from PIL import Image, ImageDraw
import os

# Set the dimensions of the flag and GIF
width, height = 600, 400
frames = 10  # Number of frames in the GIF
output_path = 'bangladesh_flag.gif'

def create_bangladesh_flag_frame(frame_index):
    # Create a new image with a green background
    img = Image.new('RGB', (width, height), '#138808')
    
    # Draw the red circle on the image
    draw = ImageDraw.Draw(img)
    circle_radius = int(min(width, height) * 0.2)
    circle_center = (width // 2, height // 2)
    circle_box = (
        circle_center[0] - circle_radius,
        circle_center[1] - circle_radius,
        circle_center[0] + circle_radius,
        circle_center[1] + circle_radius
    )
    draw.ellipse(circle_box, fill='red')
    
    return img

def create_blank_frame():
    return Image.new('RGB', (width, height), '#138808')

# Create frames for the GIF
gif_frames = []
for i in range(frames):
    if i % 2 == 0:
        gif_frames.append(create_bangladesh_flag_frame(i))
    else:
        gif_frames.append(create_blank_frame())

# Save the GIF
gif_frames[0].save(
    output_path,
    save_all=True,
    append_images=gif_frames[1:],
    loop=0,  # Loop forever
    duration=500  # Time duration for each frame in milliseconds
)

print(f"GIF saved as '{output_path}'")

# Display the GIF
os.system(output_path)
