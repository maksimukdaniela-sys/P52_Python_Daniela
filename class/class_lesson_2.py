class Room:
    def __init__(self, number, room_type, price_per_day):
        self.number = number
        self.room_type = room_type
        self.price_per_day = price_per_day
        self.is_busy = False

    def info(self):
        status = "ЗАЙНЯТА" if self.is_busy else "ВІЛЬНА"
        print(f"Кімната {self.number} | {self.room_type} | {self.price_per_day} грн/доба | {status}")

    def set_busy(self):
        self.is_busy = True

    def set_free(self):
        self.is_busy = False


class Guest:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        print(f"Гість: {self.name}, телефон: {self.phone}")


class Booking:
    def __init__(self, guest, room, nights):
        self.guest = guest
        self.room = room
        self.nights = nights

    def get_total_price(self):
        return self.nights * self.room.price_per_day

    def info(self):
        print(
            f"Гість: {self.guest.name} | "
            f"Кімната: {self.room.number} | "
            f"Діб: {self.nights} | "
            f"Сума: {self.get_total_price()} грн"
        )


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_free_rooms(self):
        print("\nВільні кімнати:")
        for room in self.rooms:
            if not room.is_busy:
                room.info()

    def create_booking(self, guest, room_number, nights):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_busy:
                    print(f"\nКімната {room_number} вже зайнята. Бронювання неможливе.")
                    return

                booking = Booking(guest, room, nights)
                self.bookings.append(booking)
                room.set_busy()

                print("\nБронювання створено:")
                booking.info()
                return

        print("\nКімнату з таким номером не знайдено.")

    def show_bookings(self):
        print("\nУсі бронювання:")
        for booking in self.bookings:
            booking.info()


hotel = Hotel("Sunrise Hotel")

hotel.add_room(Room(101, "single", 800))
hotel.add_room(Room(102, "double", 1200))
hotel.add_room(Room(201, "lux", 2200))

anton = Guest("Антон", "+380111111111")
maria = Guest("Марія", "+380222222222")

hotel.show_free_rooms()

hotel.create_booking(anton, 101, 3)
hotel.create_booking(maria, 201, 2)

hotel.show_free_rooms()

hotel.show_bookings()


