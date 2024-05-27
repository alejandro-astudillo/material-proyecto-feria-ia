from groq import Groq

# Inicializa el cliente con API key
client = Groq(
    api_key="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",
)


def llama3_request(history):
    chat_completion = client.chat.completions.create(
        messages=history,
        model="llama3-70b-8192",  # -> Modelo de Llama 3 con 70B de parámetros
    )
    return chat_completion


def main():
    history = []
    print("Chat con LLaMA3. Para terinar chat escriban 'salir'")

    while True:
        user_input = input("Prompt: ")

        if user_input.lower() == 'salir':
            break

        # Agregar la entrada del usuario al historial
        history.append({"role": "user", "content": user_input})

        # Realizar la solicitud a la API
        response = llama3_request(history)
        model_reply = response.choices[0].message.content

        # Agregar la respuesta del modelo al historial
        history.append({"role": "assistant", "content": model_reply})

        # Imprimir la respuesta del modelo
        print(f"Respuesta de LLaMA3: {model_reply}")


if __name__ == "__main__":
    main()
