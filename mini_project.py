from datetime import datetime

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
    for shipment_id, details in ship_details.items():
        sender_id = int(details[0])
        receiver_id = int(details[1])
        
        sender_name = client_details.get(sender_id, "Unknown Sender")
        receiver_name = client_details.get(receiver_id, "Unknown Receiver")
        
        details[0] = sender_name
        details[1] = receiver_name 
        print(f"Shipment ID: {shipment_id}, Details: {details}")


def sender_display_shipments(ship_details,client_details):
    name=input("Enter Client Name to display shipments:")
    for shipment_id, details in ship_details.items():
        sender_name = details[0]
        receiver_name = details[1]
        
        if sender_name == name:
            print(f"Shipment ID: {shipment_id}, Details: {details}")


def receiver_display_shipments(ship_details,client_details):
    name=input("Enter Client Name to display shipments:")
    for shipment_id, details in ship_details.items():
        sender_name = details[0]
        receiver_name = details[1]
        
        if receiver_name == name:
            print(f"Shipment ID: {shipment_id}, Details: {details}")


def delivery_status_display(ship_details,client_details):
    status=input("Enter Delivery Status to display shipments:")
    for shipment_id, details in ship_details.items():
        delivery_status = details[6]
        
        if delivery_status == status:
            print(f"Shipment ID: {shipment_id}, Details: {details}")


def delivered_in_7days(ship_details,client_details):
    for shipment_id, details in ship_details.items():
        start_date = details[2]
        delivery_date = details[3]
        
        # Assuming the dates are in the format 'DD_MM_YYYY', you can parse them using datetime.strptime
        from datetime import datetime
        
        start_date_obj = datetime.strptime(start_date, '%d_%m_%Y')
        delivery_date_obj = datetime.strptime(delivery_date, '%d_%m_%Y')
        
        days_difference = (delivery_date_obj - start_date_obj).days
        
        if days_difference <= 7:
            print(f"Shipment ID: {shipment_id}, Details: {details}, Delivered in {days_difference} days")






ship_det(shipment_Id)
print(ship_details)


client_id=int(input("Enter your Client ID:"))
client_details={}

client_det(client_id)

print(client_details)

change_id_to_name(ship_details,client_details)

sender_display_shipments(ship_details,client_details)
receiver_display_shipments(ship_details,client_details)
delivery_status_display(ship_details,client_details)
delivered_in_7days(ship_details,client_details)


