# What is HLR?

The Home Location Register (HLR) is a database that contains data related to customers authorized to use the Global System for Mobile Communications (GSM) network.

Some of the information stored in the HLR includes the International Mobile Subscriber Identity (IMSI) and the International Mobile Subscriber Directory Number (MSISDN) of each subscription.

So HLR in a nutshell

HLR is a mobile network information database. HLR is an integral component of GSM, CDMA, and TDMA networks. This method is not a method for tracking location, but rather the area where a cellphone number comes from based on a unique code set by each cellular operator.

Is that accurate?

HLR will never be accurate. HLR will only show the location of the city where the number was issued or registered, not the location where we are now

# What is IMSI? 

The IMSI uniquely identifies each Subscriber Identity Module (SIM) and serves as the primary key for each record in the HLR

# What is MSISDN

MSISDN (also known as Mobile Station International Subscriber Directory Number) is a list of telephone numbers for each subscription 

# So what HLR for?

1. HLR is updated whenever the SIM is transferred to another location area.

2. HLR also plays a crucial role in the delivery of Short Message Service (SMS) messages.

3. Before an SMS company forwards a message to the intended recipient, it scans through the HLR to find the recently used Mobile Switching Center (MSC).

4. If the target MSC reports that the recipient's phone is unavailable, a message waiting flag is set in the HLR.

5. If the recipient appears in another MSC (for example, when traveling to another city), they still receive the message because the MSC notifies the HLR once the recipient is detected within its jurisdiction.

6. Other mobile components actively working with the HLR include the Gateway Mobile Switching Center (G-MSC), Visitor Location Register (VLR), and Authentication Center (AUC).

# What is BTS?

A base transceiver station (BTS) or a baseband unit[1] (BBU) is a piece of equipment that facilitates wireless communication between user equipment (UE) and a network. UEs are devices like mobile phones (handsets), WLL phones, computers with wireless Internet connectivity, or antennas mounted on buildings or telecommunication towers. The network can be that of any of the wireless communication technologies like GSM, CDMA, wireless local loop, Wi-Fi, WiMAX or other wide area network (WAN) technology.

BTS is also referred to as the node B (in 3G networks) or, simply, the base station (BS). For discussion of the LTE standard the abbreviation eNB for evolved node B is widely used, and GNodeB for 5G.

Though the term BTS can be applicable to any of the wireless communication standards, it is generally associated with mobile communication technologies like GSM and CDMA. In this regard, a BTS forms part of the base station subsystem (BSS) developments for system management. It may also have equipment for encrypting and decrypting communications, spectrum filtering tools (band pass filters) and so on. Antennas may also be considered as components of BTS in general sense as they facilitate the functioning of BTS. Typically a BTS will have several transceivers (TRXs) which allow it to serve several different frequencies and different sectors of the cell (in the case of sectorised base stations). A BTS is controlled by a parent base station controller via the base station control function (BCF). The BCF is implemented as a discrete unit or even incorporated in a TRX in compact base stations. The BCF provides an operations and maintenance (O&M) connection to the network management system (NMS), and manages operational states of each TRX, as well as software handling and alarm collection. The basic structure and functions of the BTS remains the same regardless of the wireless technologies.

# What is Triangulation

Curiulation in Cell Phone Tracking:

Triangulation is a mathematical technique used to determine the location of an object using information from at least three known reference points. In the context of cell phone tracking, triangulation involves using data from multiple sources, such as cellular signals, GPS, and Wi-Fi, to determine a cell phone's location with fairly high accuracy. Not just anyone can do it because it requires sensitive data such as IMEI, LAC, CID, etc. which are only accepted by the provider/network provider. However, it can still be used by the police because they are the authorities.

Triangulation is so named because conceptually it looks like forming a triangle using three BTS towers that are simultaneously connected to our cellphone.

Each BTS tower is divided into three sectors, which we can call the Alpha, Beta and Gamma sectors (α, ß, Y). Each sector is used to measure the distance from the user's location to the BTS tower.

# Notes
>
>I will make changes to the article here and review it and add case study examples
>

# Reffernce 

- [Forum Seccodeid Trace Cell Phone Num](https://forum.seccodeid.com/d/mencari-dan-melacak-nomor-hp-dengan-teknik-osint)
- [What is BTS](https://en.wikipedia.org/wiki/Base_transceiver_station)
- [cell phone triangulation](https://www.linkedin.com/pulse/cell-phone-triangulation-boney-maundu/)
- [Triangulation Cell Work TegalSec Blog](https://blog.tegalsec.org/methode-melacak-ponsel-triangulating-with-bts-for-swift-recovery/)

