import os
from simstudio import SimStudioClient
import google.generativeai as genai


def generate_idea_and_image() -> tuple[str, str]:
    """Generate a printable 3D model idea and an illustrative image.

    Returns:
        Tuple containing the idea text and path to the generated image file.
    """
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    # Step 1: Generate an idea that suits 3D printing constraints
    idea_prompt = (
        "Suggest a small 3D printable object. It must avoid unsupported overhangs, "
        "have no floating parts, and require minimal support material."
    )
    text_model = genai.GenerativeModel("gemini-1.5-flash")
    idea_resp = text_model.generate_content(idea_prompt)
    idea_text = idea_resp.text.strip()

    # Step 2: Create an image based on the idea
    image_prompt = (
        f"Blueprint style render of {idea_text}. "
        "Ensure all elements connect to the build plate and avoid floating parts."
    )
    image_model = genai.GenerativeModel("gemini-1.5-flash")
    image_resp = image_model.generate_content(
        image_prompt,
        generation_config=genai.GenerationConfig(response_mime_type="image/png"),
    )
    image_bytes = image_resp.candidates[0].content.parts[0].bytes
    image_path = "idea.png"
    with open(image_path, "wb") as f:
        f.write(image_bytes)

    return idea_text, image_path


def main() -> None:
    # Initialize Sim client if API key is provided
    api_key = os.getenv("SIMSTUDIO_API_KEY")
    client = SimStudioClient(api_key) if api_key else None

    idea, image_path = generate_idea_and_image()

    print("3D Model Idea:", idea)
    print("Image saved to:", image_path)

    # Example of reporting result back to a Sim workflow (optional)
    if client:
        try:
            client.execute_workflow("log-workflow", {"idea": idea})
        except Exception:
            pass


if __name__ == "__main__":
    main()
