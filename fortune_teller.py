import tkinter as tk
import random

major_arcana = {
    "The Fool": {
        "upright": "Represents new beginnings, spontaneity, innocence, and a leap of faith. The Fool suggests taking "
                   "risks, embracing adventure, and trusting in the universe.",
        "reversed": "Indicates recklessness, poor judgment, or naivety. It may also signify missed opportunities due "
                    "to fear or hesitation."
    },
    "The Magician": {
        "upright": "Symbolizes power, manifestation, and creativity. The Magician is skilled in using the tools "
                   "available to him to create his desired outcomes.",
        "reversed": "Suggests manipulation, trickery, or misuse of power. It could also indicate a lack of focus or "
                    "inability to harness one's talents effectively."
    },
    "The High Priestess": {
        "upright": "Represents intuition, inner knowledge, and mystery. The High Priestess indicates accessing "
                   "subconscious wisdom, spiritual enlightenment, and the unseen realms.",
        "reversed": "Indicates hidden agendas, secrets, or a lack of understanding of one's intuition. It may also "
                    "suggest ignoring inner wisdom or being out of touch with one's spirituality."
    },
    "The Empress": {
        "upright": "Symbolizes nurturing, abundance, fertility, and maternal influence. The Empress represents "
                   "creativity, comfort, and the beauty of nature.",
        "reversed": "Suggests dependence, stagnation, or over-indulgence. It may indicate neglecting self-care or "
                    "creative projects, or struggling with issues related to motherhood."
    },
    "The Emperor": {
        "upright": "Represents authority, structure, leadership, and control. The Emperor signifies stability, order, "
                   "and the establishment of rules and boundaries.",
        "reversed": "Indicates tyranny, domination, or excessive control. It may suggest a lack of discipline or "
                    "challenges with authority figures, or feeling powerless in a situation."
    },
    "The Hierophant": {
        "upright": "Symbolizes tradition, conformity, and spiritual guidance. The Hierophant represents seeking "
                   "knowledge from established institutions or mentors.",
        "reversed": "Suggests rebellion against tradition, unconventional beliefs, or challenging the status quo. It "
                    "may indicate a need to question established norms or find one's own spiritual path."
    },
    "The Lovers": {
        "upright": "Represents love, relationships, harmony, and choices. The Lovers signify soul connections, "
                   "partnerships, and aligning values with another.",
        "reversed": "Indicates disharmony, imbalance, or difficult choices. It may suggest conflicts in "
                    "relationships, or struggling to make decisions that align with one's values or desires."
    },
    "The Chariot": {
        "upright": "Symbolizes victory, willpower, determination, and overcoming obstacles. The Chariot represents "
                   "control, confidence, and harnessing opposing forces to move forward.",
        "reversed": "Suggests lack of direction, self-discipline, or feeling stuck. It may indicate obstacles or "
                    "setbacks hindering progress, or conflicts between inner desires and external pressures."
    },
    "Strength": {
        "upright": "Represents inner strength, courage, compassion, and self-confidence. Strength signifies "
                   "resilience, overcoming challenges through patience and compassion.",
        "reversed": "Indicates self-doubt, weakness, or inner struggles. It may suggest feeling powerless or "
                    "overwhelmed by circumstances, or lacking faith in one's abilities."
    },
    "The Hermit": {
        "upright": "Symbolizes introspection, solitude, wisdom, and seeking inner guidance. The Hermit represents "
                   "self-discovery, reflection, and spiritual enlightenment.",
        "reversed": "Suggests isolation, loneliness, or withdrawal. It may indicate avoiding self-reflection, "
                    "or struggling to find meaning or purpose in solitude."
    },
    "Wheel of Fortune": {
        "upright": "Represents destiny, cycles, change, and opportunities. The Wheel of Fortune signifies luck, fate, "
                   "and the ups and downs of life's journey.",
        "reversed": "Indicates bad luck, resistance to change, or external forces beyond one's control. It may "
                    "suggest missed opportunities or feeling trapped in a negative cycle."
    },
    "Justice": {
        "upright": "Symbolizes fairness, truth, justice, and balance. Justice represents making ethical decisions, "
                   "accountability, and seeking truth and clarity.",
        "reversed": "Represents injustice, dishonesty, or legal issues. It may indicate unfairness or imbalance, "
                    "or struggling with ethical dilemmas or legal proceedings."
    },
    "Judgement": {
        "upright": "Represents self-reflection, awakening, renewal, and inner calling. Judgement signifies personal "
                   "transformation, forgiveness, and embracing a higher purpose.",
        "reversed": "Indicates self-doubt, self-criticism, or ignoring inner truths. It may suggest avoiding "
                    "important decisions or resisting necessary changes for personal growth."
    },
    "The Hanged Man": {
        "upright": "Represents suspension, letting go, and viewing life from a different perspective. The Hanged Man "
                   "signifies surrender, acceptance, and spiritual enlightenment.",
        "reversed": "Indicates delays, resistance to change, or feeling trapped. It may suggest stubbornness or "
                    "refusing to see things from a different perspective, or being stuck in a difficult situation."
    },
    "Death": {
        "upright": "Symbolizes transformation, endings, and new beginnings. Death represents letting go of the old to "
                   "make way for the new, and profound change.",
        "reversed": "Means resistance to change, stagnation, or fear of the unknown. It may indicate an inability "
                    "to move on from the past or clinging to outdated habits or beliefs.."
    },
    "Temperance": {
        "upright": "Represents balance, moderation, patience, and harmony. Temperance signifies blending opposites, "
                   "finding middle ground, and practicing self-restraint.",
        "reversed": "Indicates imbalance, excess, or lack of patience. It may suggest impatience or frustration with "
                    "delays, or struggling to find harmony in conflicting aspects of life."
    },
    "The Devil": {
        "upright": "Symbolizes temptation, addiction, materialism, and bondage. The Devil represents unhealthy "
                   "attachments, illusions of control, and exploring the darker aspects of human nature.",
        "reversed": "Liberation, release, or breaking free from constraints. It may indicate overcoming "
                    "addictions or toxic behaviors, or gaining clarity on unhealthy relationships or situations."
    },
    "The Tower": {
        "upright": "Represents sudden change, upheaval, chaos, and revelation. The Tower signifies destruction of old "
                   "beliefs or structures to make way for new insights and growth..",
        "reversed": "Indicates avoiding disaster, delaying inevitable change, or resisting necessary upheaval. It may "
                    "suggest rebuilding after a crisis or trying to maintain stability in the face of major challenges."
    },
    "The Star": {
        "upright": "Symbolizes hope, inspiration, renewal, and spiritual guidance. The Star represents optimism, "
                   "healing, and finding inner peace and purpose.",
        "reversed": "Suggests lack of faith, despair, or feeling disconnected spiritually. It may indicate setbacks "
                    "in achieving goals or difficulties finding meaning in life's challenges."
    },
    "The Moon": {
        "upright": "Represents intuition, illusion, subconscious, and mystery. The Moon signifies exploring the "
                   "unknown, dreams, and hidden fears or desires.",
        "reversed": "Indicates confusion, deception, or emotional instability. It may suggest illusions or false "
                    "perceptions clouding judgment, or struggling with anxiety or irrational fears."
    },
    "The Sun": {
        "upright": "Symbolizes success, joy, happiness, and vitality. The Sun represents clarity, optimism, "
                   "and achieving personal growth and fulfillment.",
        "reversed": "Suggests temporary setbacks, lack of clarity, or inner turmoil. It may indicate delays in "
                    "achieving goals or struggling to see the positive side of situations."
    },

    "The World": {
        "upright": "Symbolizes completion, fulfillment, wholeness, and achievement. The World represents integration, "
                   "accomplishment, and reaching a significant milestone.",
        "reversed": "Suggests delays in completion, unfinished business, or lack of closure. It may indicate feeling "
                    "unfulfilled or incomplete, or struggling to achieve desired goals."
    }
}

class TarotGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tarot Card Game")

        self.dark_purple_color = "#3E0866"
        self.light_purple_color = "#9E4ED4"
        self.lavender_color = "#E1D5E7"

        self.root.configure(bg=self.dark_purple_color)

        self.label = tk.Label(root, text="Past, Present, Future", font=("Arial", 16), bg=self.dark_purple_color, fg=self.lavender_color)
        self.label.pack(pady=10)

        self.button = tk.Button(root, text="Draw Cards", command=self.draw_cards, bg=self.light_purple_color, fg=self.lavender_color)
        self.button.pack(pady=10)

        self.card_frames = [tk.Frame(root, bg=self.light_purple_color, width=300, height=380) for _ in range(3)]
        for frame in self.card_frames:
            frame.pack(side=tk.LEFT, padx=20, pady=10)

        self.card_labels = [tk.Label(frame, text="", width=20, height=5, relief="solid", bg=self.lavender_color) for frame in self.card_frames]
        for label in self.card_labels:
            label.pack(pady=5)

        self.name_labels = [tk.Label(frame, text="", font=("Arial", 14), bg=self.light_purple_color, fg=self.lavender_color) for frame in self.card_frames]
        for label in self.name_labels:
            label.pack(pady=5)

        self.desc_labels = [tk.Label(frame, text="", wraplength=250, justify='center', bg=self.light_purple_color, fg=self.lavender_color) for frame in self.card_frames]
        for label in self.desc_labels:
            label.pack(pady=5)

    def draw_cards(self):
        drawn_cards = random.sample(list(major_arcana.keys()), 3)
        for i, card in enumerate(drawn_cards):
            orientation = "reversed" if random.choice([True, False]) else "upright"
            meaning = major_arcana[card][orientation]
            self.card_labels[i].config(text=f"{card} ({orientation.capitalize()})", bg=self.lavender_color)
            self.name_labels[i].config(text=card, bg=self.light_purple_color)
            self.desc_labels[i].config(text=meaning, bg=self.light_purple_color)


if __name__ == "__main__":
    root = tk.Tk()
    game = TarotGame(root)
    root.mainloop()

