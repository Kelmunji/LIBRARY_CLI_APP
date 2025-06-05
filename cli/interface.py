import argparse
from database.session import SessionLocal
from models import book, member, rental

def main_cli():
    parser = argparse.ArgumentParser(description="Library CLI App")
    parser.add_argument("action", choices=["list_books", "list_members", "list_rentals"])
    args = parser.parse_args()

    db = SessionLocal()
    if args.action == "list_books":
        for b in db.query(book.Book).all():
            print(f"{b.id}: {b.title} by {b.author} - {'Available' if b.available else 'Rented'}")
    elif args.action == "list_members":
        for m in db.query(member.Member).all():
            print(f"{m.id}: {m.name} ({m.email})")
    elif args.action == "list_rentals":
        for r in db.query(rental.Rental).all():
            print(f"Rental {r.id}: Book ID {r.book_id} -> Member ID {r.member_id}")
    db.close()