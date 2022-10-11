# first commit

# Here are some of the concepts for particle system:
# • Developing a mathematical model for a fountain particle system
# • Using GPU shaders for computation
# • Using textures and billboarding to imitate complex 3D objects
# • Using OpenGL rendering features such as blending, depth masks, and alpha channels to draw semitransparent objects
# • Using a camera model to draw 3D perspective views

# Working

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
# To animate the fountain of sparks, draw the positions of the particle system at regular time intervals.

# Code
import sys, random, math
import OpenGL
from OpenGL.GL import *
import numpy
import glutils
# Defining the Particle Geometry
# create Vertex Array Object (VAO)
    self.vao = glGenVertexArrays(1)
# bind VAO
    glBindVertexArray(self.vao)
# vertices
    s = 0.2
    quadV = [
            -s, s, 0.0,
            -s, -s, 0.0,
            s, s, 0.0,
            s, -s, 0.0,
            s, s, 0.0,
            -s, -s, 0.0
            ]
    vertexData = numpy.array(numP*quadV, numpy.float32)
    self.vertexBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.vertexBuffer)
    glBufferData(GL_ARRAY_BUFFER, 4*len(vertexData), vertexData,
                GL_STATIC_DRAW)
# texture coordinates
    quadT = [
            0.0, 1.0,
            0.0, 0.0,
            1.0, 1.0,
            1.0, 0.0,
            1.0, 1.0,
            0.0, 0.0
            ]
    tcData = numpy.array(numP*quadT, numpy.float32)
    self.tcBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.tcBuffer)
    glBufferData(GL_ARRAY_BUFFER, 4*len(tcData), tcData, GL_STATIC_DRAW)

# Defining the Time-Lag Array for the Particles
# time lags
    timeData = numpy.repeat(0.005*numpy.arange(numP, dtype=numpy.float32),4)
    self.timeBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.timeBuffer)
    glBufferData(GL_ARRAY_BUFFER, 4*len(timeData), timeData,
                GL_STATIC_DRAW)

# Setting the Initial Particle Velocities
# velocites
    velocities = []
# cone angle
    coneAngle = math.radians(20.0)
# set up particle velocities
    for i in range(numP):
# inclination
        angleRatio = random.random()
        a = angleRatio*coneAngle
# azimuth
        t = random.random()*(2.0*math.pi)
# get velocity on sphere
        vx = math.sin(a)*math.cos(t)
        vy = math.sin(a)*math.sin(t)
        vz = math.cos(a)
# speed decreases with angle
        speed = 15.0*(1.0 - angleRatio*angleRatio)
# add a set of calculated velocities
        velocities += 6*[speed*vx, speed*vy, speed*vz]
# set up velocity vertex buffer
    self.velBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, self.velBuffer)
    velData = numpy.array(velocities, numpy.float32)
    glBufferData(GL_ARRAY_BUFFER, 4*len(velData), velData, GL_STATIC_DRAW)