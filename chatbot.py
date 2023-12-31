import spacy 

nlp = spacy.load("en_core_web_sm")

# Intenciones y respuestas
RESPONSES = {
    "greeting": "¡Hola! Soy un desarrollador de aplicaciones y sitios web con amplia experiencia. ¿Cómo puedo ayudarte?",
    "services": "Ofrezco una gama completa de servicios de desarrollo, incluyendo desarrollo web personalizado, aplicaciones móviles, y soluciones de software. Trabajo con tecnologías como Java, Python, JavaScript y PHP.",
    "experience": "Tengo experiencia en desarrollo web, desarrollo de aplicaciones, y además con análisis de datos en Power BI, manejo de bases de datos como DynamoDB, PostgreSQL, y MySQL, y desarrollo en plataformas de AWS como Lambdas y API Gateways.",
    "contact": "Puedes enviarme un email a programacionbluehat@gmail.com para hablar más sobre tu proyecto o cualquier duda que tengas.",
    "project_inquiry": "Si tienes un proyecto en mente, me encantaría escuchar más al respecto y ver cómo puedo ayudarte. Ya sea un proyecto universitario o un desarrollo más complejo, estoy aquí para asistirte.",
    "frameworks": "Utilizo una variedad de frameworks para asegurar que tu proyecto tenga una base sólida y moderna. Estoy especializado en Laravel, Flask y React JS, entre otros.",
    "web_design": "Además del desarrollo, también ofrezco servicios de diseño web. Uso herramientas como TailwindCSS y Bootstrap para crear diseños atractivos y responsivos.",
    "consultation": "Si no estás seguro de por dónde empezar o qué tecnologías usar, puedo ofrecerte una consulta para guiar tu proyecto en la dirección correcta.",
    "location": "Estoy ubicado en Guatemala, pero trabajo con clientes de todo el mundo. La distancia no es una barrera para entregar soluciones de calidad.",
    "farewell": "Gracias por tu interés. Espero tener noticias tuyas pronto. ¡Adiós!"
}

# Palabras clave para cada intención
INTENT_KEYWORDS = {
    "greeting": ["hola", "buenos días", "buenas tardes", "hey", "hello"],
    "services": ["servicios", "desarrollo", "aplicaciones", "web", "software", "lenguajes","lenguaje"],
    "experience": ["experiencia", "tecnologías", "herramientas", "aws", "bases de datos"],
    "contact": ["contacto", "email", "correo", "comunicarse","nombre","contactarte"],
    "project_inquiry": ["proyecto", "colaboración", "trabajo", "consulta"],
    "frameworks": ["frameworks", "laravel", "flask", "react","framework"],
    "web_design": ["diseño web", "frontend", "interfaz", "usuario"],
    "consultation": ["consulta", "asesoramiento", "ayuda", "orientación"],
    "location": ["ubicación", "dónde", "guatemala", "internacional"],
    "farewell": ["adiós", "gracias", "hasta luego", "bye","adios"]
}


def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        for intent, keywords in INTENT_KEYWORDS.items():
            if token.text in keywords:
                return intent
            
    return "unknown"        


def process_text(text):
    intent = get_intent(text)
    return RESPONSES.get(intent, 'lo siento, no estoy seguro de como responder a eso.')


# while True:
#     user_input = input("Tu: ")
#     if user_input.lower() in ["salir", "exit"]:
#         print('Bot: Hasta luego!')
#         break
#     if not user_input.strip():
#         print('Bot: Parece que no has ingresado nada. Puedes intentar de nuevo?')
#         continue
#     response = process_text(user_input)
#     print('Bot: ', response)