from services.rag_pipeline import generate_notes

url = input("Enter YouTube URL: ")

notes = generate_notes(url)

print("\nGenerated Notes:\n")
print(notes)