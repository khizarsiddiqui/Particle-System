# Particle-System

A fountain particle system using Python and OpenGL with implementation of shaders.
The given link helps to understand the equation of motion and its derivation:https://byjus.com/physics/derivation-of-equation-of-motion/

Images provided helps to illustrate the concept and viewpoints set according to the azimuths.
The given link helps to understand the concept of the azimuth:https://www.youtube.com/watch?v=lM6kWrgsGYw

Billboards are positionned at a specific location, but their orientation is automatically computed so that it always faces the camera.
The given link helps to understand the concept of the billboarding:http://www.opengl-tutorial.org/intermediate-tutorials/billboards-particles/billboards/

Understanding difference between orthogonal and orthonormal:https://jamesmccaffrey.wordpress.com/2019/12/14/the-difference-between-orthogonal-and-orthonormal-vectors/

To understand glGenBuffers:https://registry.khronos.org/OpenGL-Refpages/gl2.1/xhtml/glGenBuffers.xml

What is Interpolation?
In the mathematical field of numerical analysis, interpolation is a type of estimation, a method of constructing new data points based on the range of a discrete set of known data points.

Note: Textures are accessed from within shaders using samplers, and you set the sampler variable to use the first texture unit, GL_TEXTURE0. You then use OpenGL blending to cut out the black pixels in the texture, but these “invisible” pixels still have a depth value associated with them and can obscure parts of other particles that are behind them. To avoid this, disable writing to the depth buffer. This is the wrong way to draw because if you mix these semitransparent objects with opaque objects, they will not be depth tested properly. The correct way to render such a scene is to first draw the opaque objects and then enable blending, sort the semitransparent objects in depth from back to front, and draw them last. But because you have so many moving particles, this simple approximation is acceptable, and in the end, it looks fine, which is what you care about.

glBlendFunc(): defines the operation of blending. The sfactor parameter specifies which of nine methods is used to scale the source color components. The dfactor parameter specifies which of eight methods is used to scale the destination color components.

The point (r cos(θ), r sin(θ)) represents a point on a circle of radius r centered at the origin, and θ is the angle that the line from the origin to the point makes with the x-axis. The translation using center ensures this works even if your center of rotation is not at the origin.

For understanding glVertexAttribPointer() :https://registry.khronos.org/OpenGL-Refpages/gl4/html/glVertexAttribPointer.xhtml

For understanding stride in glVertexAttribPointer():https://stackoverflow.com/questions/22296510/what-does-stride-mean-in-opengles

For understanding glDrawArrays():https://registry.khronos.org/OpenGL-Refpages/gl4/html/glDrawArrays.xhtml