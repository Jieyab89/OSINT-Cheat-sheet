import configparser
import os
import requests

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")


class XquikError(Exception):
    pass


def load_config(path: str = CONFIG_PATH) -> configparser.ConfigParser:
    if not os.path.exists(path):
        raise XquikError(f"Config tidak ditemukan: {path}")
    cfg = configparser.ConfigParser()
    cfg.read(path)
    return cfg


class XquikClient:
    def __init__(self, config: configparser.ConfigParser = None):
        self.config = config or load_config()
        self.api_key = self.config.get("xquik", "api_key", fallback="").strip()
        self.base_url = self.config.get(
            # Endpoint list arr soon 
            "xquik", "base_url", fallback="https://xquik.com/api/v1/extractions"
        ).strip()

        if not self.api_key or self.api_key == "xq_YOUR_KEY":
            raise XquikError("api_key Xquik are not set")

    def _post(self, payload: dict) -> dict:
        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json",
        }
        try:
            resp = requests.post(self.base_url, headers=headers, json=payload, timeout=30)
        except requests.RequestException as e:
            raise XquikError(f"Request failed: {e}") from e

        if resp.status_code >= 400:
            raise XquikError(f"xquik API error {resp.status_code}: {resp.text}")

        try:
            return resp.json()
        except ValueError as e:
            raise XquikError(f"Response are not json: {resp.text[:300]}") from e
    
    # PARAMS IN Xquik docs 
    # https://docs.xquik.com/

    def tweet_search(self, search_query: str) -> dict:
        return self._post({"toolType": "tweet_search_extractor", "searchQuery": search_query})

    def follower_explorer(self, target_username: str) -> dict:
        return self._post({"toolType": "follower_explorer", "targetUsername": target_username})

    def article_extractor(self, target_tweet_id: str) -> dict:
        return self._post({"toolType": "article_extractor", "targetTweetId": target_tweet_id})

    def community_post_extractor(self, target_community_id: str) -> dict:
        return self._post(
            {"toolType": "community_post_extractor", "targetCommunityId": target_community_id}
        )

    def post_extractor(self, target_username: str) -> dict:
        """User timeline via Xquik"""
        return self._post({"toolType": "post_extractor", "targetUsername": target_username})


if __name__ == "__main__":
    import argparse
    import json

    # PARAMS IN Xquik docs 
    # https://docs.xquik.com/

    parser = argparse.ArgumentParser(description="xquik.com extraction CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p1 = sub.add_parser("tweet_search")
    p1.add_argument("query")

    p2 = sub.add_parser("follower_explorer")
    p2.add_argument("username")

    p3 = sub.add_parser("article_extractor")
    p3.add_argument("tweet_id")

    p4 = sub.add_parser("community_post_extractor")
    p4.add_argument("community_id")

    p5 = sub.add_parser("post_extractor")
    p5.add_argument("username")

    args = parser.parse_args()
    client = XquikClient()

    # PARAMS IN Xquik docs 
    # https://docs.xquik.com/

    try:
        if args.command == "tweet_search":
            out = client.tweet_search(args.query)
        elif args.command == "follower_explorer":
            out = client.follower_explorer(args.username)
        elif args.command == "article_extractor":
            out = client.article_extractor(args.tweet_id)
        elif args.command == "community_post_extractor":
            out = client.community_post_extractor(args.community_id)
        elif args.command == "post_extractor":
            out = client.post_extractor(args.username)
        print(json.dumps(out, indent=2, ensure_ascii=False))
    except XquikError as e:
        print(f"[ERROR] {e}")
        raise SystemExit(1)