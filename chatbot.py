from app.retriever import Retriever
from app.llm import GeminiLLM
from app.chat_memory import ChatMemory


def main():

    memory = ChatMemory()

    print("=" * 70)
    print("🩺      Insurance Document Chatbot")
    print("=" * 70)
    print("Type your question about the insurance policy.")
    print("Commands:")
    print("   history  -> Show previous conversation")
    print("   exit     -> Quit the chatbot")
    print("=" * 70)

    while True:

        question = input("\n🧑 You: ").strip()

        # Exit chatbot
        if question.lower() == "exit":
            print("\n👋 Thank you for using Insurance Document Chatbot!")
            break

        # Empty input
        if question == "":
            print("⚠ Please enter a question.")
            continue

        # Show conversation history
        if question.lower() == "history":

            history = memory.get_history()

            if len(history) == 0:
                print("\nNo conversation history found.")
                continue

            print("\n" + "=" * 70)
            print("📜 Conversation History")
            print("=" * 70)

            for index, chat in enumerate(history, start=1):

                print(f"\nConversation {index}")
                print("-" * 70)
                print(f"🧑 You : {chat['question']}")
                print(f"🤖 Bot : {chat['answer']}")

            print("=" * 70)

            continue

        try:

            # Retrieve relevant chunks
            chunks = Retriever.retrieve(question, top_k=3)

            if len(chunks) == 0:
                print("\n🤖 Bot:")
                print("Sorry, I couldn't find any relevant information.")
                continue

            # Build context
            context = ""

            for i, chunk in enumerate(chunks, start=1):
                context += f"\nDocument Chunk {i}:\n{chunk}\n"

            # Generate answer
            answer = GeminiLLM.generate_answer(
                context=context,
                question=question
            )

            # Save conversation
            memory.add(question, answer)

            # Print answer
            print("\n" + "=" * 70)
            print("🤖 Answer")
            print("=" * 70)
            print(answer)

            # ⭐ Write this HERE
            print("\n📄 Sources Used:")

            for i in range(len(chunks)):
                print(f"   ✔ Chunk {i + 1}")

            print("=" * 70)

        except Exception as e:
            print("\n❌ Error occurred:")
            print(e)