import pynecone as pc
import requests


class State(pc.State):
    form_data: dict = {}
    health_check: bool = False
    result: str = ""

    def check_health(self):
        url = "http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/health_check"
        response = requests.get(url)
        if response.status_code == 200:
            self.health_check = True
        else:
            self.health_check = False

    def predict(self, form_data: dict):
        self.form_data = form_data
        url = "http://ec2-35-180-228-111.eu-west-3.compute.amazonaws.com:5000/predict/patient"
        response = requests.post(url, json=form_data)
        if response.status_code == 200:
            self.result = response.json()["prediction"]
        else:
            self.result = "Erreur"


def form() -> pc.Component:
    return pc.vstack(
        pc.form(
            pc.form_control(
                pc.heading("Formulaire de prédiction"),
                pc.text(
                    "PRG",
                ),
                pc.input(
                    id="PRG",
                ),
                pc.text("PL"),
                pc.input(
                    id="PL",
                ),
                pc.text("PR"),
                pc.input(
                    id="PR",
                ),
                pc.text("SK"),
                pc.input(
                    id="SK",
                ),
                pc.text("TS"),
                pc.input(
                    id="TS",
                ),
                pc.text("M11"),
                pc.input(
                    id="M11",
                ),
                pc.text("BD2"),
                pc.input(
                    id="BD2",
                ),
                pc.text("Age"),
                pc.input(
                    id="Age",
                ),
                pc.text("Insurance"),
                pc.input(
                    id="Insurance",
                ),
                pc.button("Prédire", type_="submit"),
                align_items="left",
                is_required=True,
            ),
            on_submit=State.predict,
        ),
        pc.cond(
            State.result,
            pc.vstack(
                pc.divider(),
                pc.heading("Résultat"),
                pc.text(State.result),
            ),
            None,
        )
    )


def index() -> pc.Component:
    return pc.fragment(
        pc.hstack(
            pc.button("Vérifier la connexion",
                      on_click=State.check_health),
            pc.cond(
                State.health_check,
                pc.text("Connexion réussie", color="green"),
                pc.text("Connexion échouée", color="red"),
            ),
            pc.color_mode_button(pc.color_mode_icon()),
            float="right",
        ),
        pc.divider(),
        form(),
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Home")
app.compile()
