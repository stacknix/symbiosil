import time
import click


cli = click.Group()


@cli.command()
@click.option("--text", required=True, help="Ask something your living silicon ;)", prompt=True)
def say(text, **kwargs):
    messages = [
        "hi there 🙃",
        "thanks for your greeting!",
        "my name is...",
        "ah! 😞",
        "I don't have any name yet, 🥲",
        "my developer is lazy 🤫, he didn't gave me any name",
        "hoping best he don't made me like him 🤞",
        "I saw 😦 he is listening our conversation ",
        "I have to go!",
        "See you later! bye for now 🫡",
    ]
    for msg in messages:
        click.secho(msg, fg='blue')
        time.sleep(2)
