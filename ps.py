# first commit

# Here are some of the concepts for particle system:
# • Developing a mathematical model for a fountain particle system
# • Using GPU shaders for computation
# • Using textures and billboarding to imitate complex 3D objects
# • Using OpenGL rendering features such as blending, depth masks, and alpha channels to draw semitransparent objects
# • Using a camera model to draw 3D perspective views

# working

# Your particle system should have these features:
# • The particles should emerge from a fixed point, and their motion should follow the shape of a parabola.
# • The particles should be able to travel a predefined distance with respect to the vertical axis (z-axis or height) of the fountain.
# • Particles closer to the center of the fountain’s vertical axis should have larger initial velocities than those farther from the center.
# • To produce a more realistic effect, the particles should not all be ejected at the same time.
# • The brightness of the particles should fade over their lifetime.

# modeling particle
# setting maximum speed
# UNDERSTANDING range, limits and velocities of particles
# You can use 0.05 for the lag time,and 20 degrees for the maximum angle

# Rendering the Particles
# Drawing sparks from scratch is too complicated, so you’ll take a picture of a spark and paste it as a texture onto a rectangle (also called a quad).
# Using OpenGL Blending to Create More Realistic Sparks
# You can make the black regions disappear by enabling OpenGL blending and multiplying the alpha value of a fragment by the texture color.

# billboarding
# Applying this, rotation matrix aligns your textured quad correctly toward the view direction.

# Animating the Sparks
# To animate the fountain of sparks, draw the positions of the particle system at regular time intervals