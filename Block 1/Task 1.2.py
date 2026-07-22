"""
The checksum is computed by multiplying the ASCII value of each character by its position in the ticket ID,
summing all values,then taking modulo 100.
Including the position ensures that changing or swapping characters changes the checksum

"""


class TicketCodec:
    def _calc_checksum(self, ticket_id):
        checksum = 0
        for i, ch in enumerate(ticket_id):
            checksum += (i + 1) * ord(ch)
        return f"{checksum%100:02d}"

    def encode(self, ticket_id):
        final_checksum = self._calc_checksum(ticket_id)
        return f"{ticket_id}-{final_checksum}"

    def decode(self, barcode):
        try:
            ticket_id, rec_checksum = barcode.split("-")

        except ValueError:
            return "Please Enter a Valid Barcode! "

        calc_checksum = self._calc_checksum(ticket_id)
        if calc_checksum == rec_checksum:
            return f"{ticket_id} is valid! "
        else:
            return "CORRUPTED TICKET"


codec = TicketCodec()
while True:
    print("   **Stadium Ticket System**    \n")

    print("1. Encode Ticket")
    print("2. Verify Barcode")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ticket = input("Enter Ticket ID: ")
        barcode = codec.encode(ticket)
        print("Generated Barcode:", barcode)

    elif choice == "2":
        barcode = input("Enter Barcode: ")
        print(codec.decode(barcode))

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
