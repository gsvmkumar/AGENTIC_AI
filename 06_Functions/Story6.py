def serve():
    chai_type="masala"
    print(f" INside function {chai_type}")

chai_type="lemon"
serve()
print(f"Outside function {chai_type}")

def chai_counter():
    chai_order="ginger"
    def print_order():
        chai_order="MASALA"
        print("Inner ",chai_order)
    
    print_order()

    print("outer ",chai_order)

chai_order="Tulasi"
chai_counter()
print("outer  :",chai_order)