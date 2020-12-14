# Is it in the code or the way the arrays are written?
# could do individual array for each correct answer and compare input to that
#osi_layer_1 = ["1", "OSI", "Physical"]
#osi_layer_2 = ["2", "OSI", "Data Link"]
#osi_layer_3 = ["3", "OSI", "Network"]
#osi_layer_4 = ["4", "OSI", "Transport"]
#osi_layer_5 = ["5", "OSI", "Session"]
#osi_layer_6 = ["6", "OSI", "Presentation"]
#osi_layer_7 = ["7", "OSI", "Application"]

# Possible comninations osi 1-7 + tcp\ip 1-4 = 11 different arrays to create
#tci_ip_layer_1 = ["1", "Tcp/Ip", "Network Access" or "Link"]
#tci_ip_layer_2 = ["2", "Tcp/Ip", "Internet"]
#tci_ip_layer_3 = ["3", "Tcp/Ip", "Transport"]
#tci_ip_layer_4 = ["4", "Tcp/Ip", "Application"]


#answer format
"This is the ________ layer of the __________ model. This is the ____________layer "


# answers \2d array\
answers = [["1", "OSI", "Physical"],["2", "OSI", "Data Link"], ["3", "OSI", "Network"],
["4", "OSI", "Transport"],["5", "OSI", "Session"],["6", "OSI", "Presentation"],
["7", "OSI", "Application"],["1", "TCP/IP", "Network"],["2", "TCP/IP", "Internet"],
["3", "TCP/IP", "Transport"],["4", "TCP/IP", "Application"]]


# questions
model_questions = [

#q1
    "This layer is responsible for the connection (physical or wireless) between network nodes. \n"
    "It defines the cabel, connector,  or wireless technology used to connect devices.\n"
    "Also responsible for transmission of raw data (binary) while controlling bit rates.",
#q2
    "A communication between two physically linked nodes on a network is established and terminated by this layer.\n "
    "It breaks up packets into frames and transfers them from source to destination. This layer consists \n"
    "of two parts: Logical Link Control (LLC), which defines network protocols, performs error checking and synchronizes frames, and\n "
    "Media Access Control (MAC) using MAC addresses to connect devices and define permissions to transmit and receive data.",

#q3
    "This layer has two main functions.\n"
    " One is breaking up segments into network packets, and reassembling the packets on the receiving end.\n "
    "The other is routing packets by discovering the best path across a physical network.\n "
    "This layer uses network addresses (typically Internet Protocol addresses)\n "
    "to route packets to a destination node.",
#q4
    "This layer is responsible for assembling the segments on the receiving end and converting them back into session layer data.\n"
    "It is flow-regulated, transmitting data at a rate proportional to the receiving device link rates and the error monitoring system.\n"
    "This layer takes over data transmitted on the session layer, splits it into segments on the transmission end.",
#q5
    "This layer generates channels of communication between devices called sessions. \n"
    "It is responsible for opening sessions, making sure that they stay accessible and \n"
    "usable during transmission and closing them when contact stops.\n"
    "This layer can also set control points during a data transfer meaning \n"
    "devices can re-start the data transmission from the last control point if the session is interrupted.",
#q6
    "This layer is a little obsolete. It prepares data for the application layer mostly by checking format.\n"
    "It specifies how two devices may decrypt, encrypt, and compress data, such that it is properly obtained by the application.\n"
    "This layer takes any data from the application layer and prepares it for transmission over the session layer.",
#q7
    "This layer is used for end-user applications including web browsers and e-mail clients.\n"
    "It offers protocols to provide users with the appropriate data to allow information to be transmitted and retrieved by machines.\n"
    "A few examples of this layer include the Hypertext Transference Protocol (HTTP), the File Transfer Protocol\n"
    "(FTP), the Post Office Protocol (POP), the SMTP and the Domain Name System Protocol.",
#q8
    "This layer combines the OSI model’s L1 and L2.",
#q9
    "This layer is similar to the OSI model’s L3.",
#q10
    "Also called the Host-to-Host layer. This layer is similar to the OSI model’s L4.",
#q11
    "Also called the Process layer, this layer combines the OSI model’s L5, L6, and L7."
]
