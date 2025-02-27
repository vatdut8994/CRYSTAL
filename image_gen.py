from mflux import Flux1, Config
import time

# Load the model
flux = Flux1.from_alias(
   alias="schnell",  # "schnell" or "dev"
   quantize=4,       # 4 or 8
)

# Generate an image
def generate_image(prompt):
    image = flux.generate_image(
    seed=2,
    prompt=prompt,
    config=Config(
        num_inference_steps=2,  # "schnell" works well with 2-4 steps, "dev" works well with 20-25 steps
        height=1024,
        width=1024,
    )
    )
    image.save(path="image.png")

start = time.time()
generate_image("A beautiful landscape with a lake and a mountain in the background")
print(time.time() - start, "seconds")