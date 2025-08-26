# sim3dmodel

This repository demonstrates a simple workflow using the [Sim](https://sim.ai) Python SDK and Google Gemini to ideate a 3D-printable model and generate a reference image.

## Setup

1. Install dependencies:
   ```bash
   pip install simstudio-sdk google-generativeai
   ```
   If `simstudio-sdk` is not available via PyPI, install it from the `packages/python-sdk` directory of the cloned Sim repository.

2. Set environment variables for the APIs:
   ```bash
   export GOOGLE_API_KEY=<your_google_api_key>
   # optional: export SIMSTUDIO_API_KEY=<your_sim_api_key>
   ```

3. Run the workflow:
   ```bash
   python workflow.py
   ```

The script prints a 3D-printable idea and saves an illustrative image to `idea.png`.

