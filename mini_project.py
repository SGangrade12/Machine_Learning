shipment_Id=int(input("Enter your Shipment ID:"))
ship_details={}
def ship_det(shipment_id):
    while shipment_id!=0:
        sender=int(input("Enter Sender:"))
        receiver=int(input("Enter Receiver:"))
        start_date=input("Enter Start Date:")
        delivery_date=input("Enter Delivery Date:")
        sender_location=input("Enter sender location:")
        receiver_location=input("Enter receiver location:")
        delivery_status=input("Enter delivery status:")
        shipping_cost=int(input("Enter shipping cost:"))
        li=[str(sender),str(receiver),start_date,delivery_date,sender_location,receiver_location,delivery_status,shipping_cost]

        ship_details[shipment_id]=li
        shipment_id = int(input("Enter your Shipment ID:"))


def client_det(client_id):
    while client_id!=0:
        client_name=input("Enter Client Name:")
        client_details[client_id]=client_name
        client_id=int(input("Enter your Client ID:"))


def change_id_to_name(ship_details,client_details):
    for li in ship_details:
        if li[1] in client_details:
            ship_details[li[1]]=client_details[li[1]]






ship_det(shipment_Id)
print(ship_details)


client_id=int(input("Enter your Client ID:"))
client_details={}

client_det(client_id)

print(client_details)

change_id_to_name(ship_details,client_details)

