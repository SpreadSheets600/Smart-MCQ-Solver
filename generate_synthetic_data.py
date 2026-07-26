import csv
import random
import os

SEED = 42
random.seed(SEED)

QUESTIONS = [
    {
        "prompt": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid", "Rome"],
        "answer": "B",
    },
    {
        "prompt": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Jupiter", "Mars", "Saturn", "Mercury"],
        "answer": "C",
    },
    {
        "prompt": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue whale", "Giraffe", "Great white shark", "Hippopotamus"],
        "answer": "B",
    },
    {
        "prompt": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "NaCl", "O2", "N2"],
        "answer": "A",
    },
    {
        "prompt": "Who wrote Romeo and Juliet?",
        "options": ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain", "Ernest Hemingway"],
        "answer": "C",
    },
    {
        "prompt": "What is the speed of light in vacuum?",
        "options": ["3 x 10^6 m/s", "3 x 10^8 m/s", "3 x 10^10 m/s", "3 x 10^5 m/s", "3 x 10^7 m/s"],
        "answer": "B",
    },
    {
        "prompt": "Which of the following is NOT a programming language?",
        "options": ["Python", "Java", "Banana", "C++", "Rust"],
        "answer": "C",
    },
    {
        "prompt": "What is the powerhouse of the cell?",
        "options": ["Nucleus", "Ribosome", "Mitochondria", "Golgi apparatus", "Endoplasmic reticulum"],
        "answer": "C",
    },
    {
        "prompt": "Which element has atomic number 1?",
        "options": ["Helium", "Hydrogen", "Lithium", "Carbon", "Oxygen"],
        "answer": "B",
    },
    {
        "prompt": "What is the square root of 144?",
        "options": ["10", "11", "12", "13", "14"],
        "answer": "C",
    },
]

TEMPLATES = [
    "Pick the best possible answer: {question} based on the given context.",
    "Select the most accurate option: {question} from the following choices.",
    "Determine the correct option: {question} among the listed options.",
    "Choose the right answer: {question}",
    "What is the correct answer: {question}?",
]

SCIENCE_TERMS = [
    ("photosynthesis", "the process by which plants convert light into chemical energy", ["Respiration", "Photosynthesis", "Fermentation", "Digestion", "Combustion"], 1),
    ("gravity", "the force that attracts objects with mass toward each other", ["Magnetism", "Friction", "Gravity", "Centrifugal force", "Tension"], 2),
    ("DNA", "the molecule that carries genetic instructions in living organisms", ["RNA", "DNA", "ATP", "Protein", "Lipid"], 1),
    ("evaporation", "the process of liquid turning into gas", ["Condensation", "Sublimation", "Evaporation", "Freezing", "Melting"], 2),
    ("neutron", "the subatomic particle with no electric charge found in the nucleus", ["Proton", "Electron", "Neutron", "Positron", "Photon"], 2),
]

MATH_TERMS = [
    ("Pythagorean theorem", "the relation between sides of a right-angled triangle", ["a+b=c", "a^2+b^2=c^2", "a*b=c", "a/b=c", "a-b=c"], 1),
    ("prime number", "a number greater than 1 divisible only by 1 and itself", ["6", "9", "7", "15", "21"], 2),
    ("area of a circle", "the formula for the area of a circle", ["2*pi*r", "pi*r^2", "pi*d", "2*pi*r^2", "pi*r"], 1),
]

GEOGRAPHY_TERMS = [
    ("longest river", "the longest river in the world", ["Amazon", "Nile", "Yangtze", "Mississippi", "Danube"], 1),
    ("highest mountain", "the highest mountain peak on Earth", ["K2", "Mount Everest", "Kangchenjunga", "Lhotse", "Makalu"], 1),
    ("largest continent", "the largest continent by land area", ["Africa", "North America", "Asia", "Europe", "Antarctica"], 2),
]

HISTORY_TERMS = [
    ("first moon landing", "the year of the first human moon landing", ["1965", "1969", "1972", "1967", "1971"], 1),
    ("World War II end", "the year World War II ended", ["1943", "1944", "1945", "1946", "1947"], 2),
]


def shuffle_options(options: list, correct_idx: int) -> tuple:
    indexed = list(enumerate(options))
    random.shuffle(indexed)
    shuffled = [opt for _, opt in indexed]
    new_correct = shuffled.index(options[correct_idx])
    return shuffled, new_correct


def generate_rows(num_rows: int) -> list:
    rows = []
    label_map = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E"}

    for i in range(1, num_rows + 1):
        category = random.random()

        if category < 0.3 and QUESTIONS:
            q = random.choice(QUESTIONS)
            prompt = q["prompt"]
            options = list(q["options"])
            shuffled, correct_idx = shuffle_options(options, ord(q["answer"]) - ord("A"))
            answer = label_map[correct_idx]

        elif category < 0.5:
            term, desc, options, correct_idx = random.choice(SCIENCE_TERMS)
            template = random.choice(TEMPLATES)
            prompt = template.format(question=f"What is {desc}")
            shuffled, correct_idx = shuffle_options(list(options), correct_idx)
            answer = label_map[correct_idx]

        elif category < 0.65:
            term, desc, options, correct_idx = random.choice(MATH_TERMS)
            template = random.choice(TEMPLATES)
            prompt = template.format(question=desc)
            shuffled, correct_idx = shuffle_options(list(options), correct_idx)
            answer = label_map[correct_idx]

        elif category < 0.8:
            term, desc, options, correct_idx = random.choice(GEOGRAPHY_TERMS)
            template = random.choice(TEMPLATES)
            prompt = template.format(question=desc)
            shuffled, correct_idx = shuffle_options(list(options), correct_idx)
            answer = label_map[correct_idx]

        else:
            term, desc, options, correct_idx = random.choice(HISTORY_TERMS)
            template = random.choice(TEMPLATES)
            prompt = template.format(question=desc)
            shuffled, correct_idx = shuffle_options(list(options), correct_idx)
            answer = label_map[correct_idx]

        rows.append({
            "id": i,
            "prompt": prompt,
            "A": shuffled[0],
            "B": shuffled[1],
            "C": shuffled[2],
            "D": shuffled[3],
            "E": shuffled[4],
            "answer": answer,
        })

    return rows


def write_csv(rows, filepath: str):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "prompt", "A", "B", "C", "D", "E", "answer"])
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {filepath}")


if __name__ == "__main__":
    train_rows = generate_rows(200)
    test_rows = generate_rows(50)
    write_csv(train_rows, "Data/train_synthetic.csv")
    write_csv(test_rows, "Data/test_synthetic.csv")
