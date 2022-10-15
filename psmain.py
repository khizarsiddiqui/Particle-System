# The Code for the Main Program

from asyncio.windows_events import NULL
import sys, os, math, numpy
import OpenGL
from OpenGL.GL import *
import numpy    
from ps import ParticleSystem, Camera
from box import Box
import glutils
import glfw


class PSMaker:
    """GLFW Rendering window class for Particle System"""
    def __init__(self):
        self.camera = Camera([15.0, 0.0, 2.5],
                             [0.0, 0.0, 2.5],
                             [0.0, 0.0, 1.0])
        self.aspect = 1.0
        self.numP = 300
        self.t = 0
        # flag to rotate camera view
        self.rotate = True

        # save current working directory
        cwd = os.getcwd()

        # initialize glfw - this changes cwd
        glfw.init()
        
        # restore cwd
        os.chdir(cwd)

        # version hints
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, 
                        glfw.OPENGL_CORE_PROFILE)

        # make a window
        self.width, self.height = 640, 480
        self.aspect = self.width/float(self.height)
        self.win = glfw.create_window(self.width, self.height, 
                                     b"Particle System", NULL, NULL)
        # make context current
        glfw.make_context_current(self.win)
        
        # initialize GL
        glViewport(0, 0, self.width, self.height)
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.2, 0.2, 0.2,1.0)

        # set window callbacks
        glfw.set_mouse_button_callback(self.win, self.onMouseButton)
        glfw.set_key_callback(self.win, self.onKeyboard)
        glfw.set_window_size_callback(self.win, self.onSize)        

        # create 3D
        self.psys = ParticleSystem(self.numP)
        self.box = Box(1.0)

        # exit flag
        self.exitNow = False

        
    def onMouseButton(self, win, button, action, mods):
        #print 'mouse button: ', win, button, action, mods
        pass
    # keyboard handler
    def onKeyboard(self, win, key, scancode, action, mods):
        #print 'keyboard: ', win, key, scancode, action, mods
        if action == glfw.PRESS:
            # ESC to quit
            if key == glfw.KEY_ESCAPE: 
                self.exitNow = True
            elif key == glfw.KEY_R:
                self.rotate = not self.rotate
            elif key == glfw.KEY_B:
                # toggle billboarding
                self.psys.enableBillboard = not self.psys.enableBillboard
            elif key == glfw.KEY_D:
                # toggle depth mask
                self.psys.disableDepthMask = not self.psys.disableDepthMask
            elif key == glfw.KEY_T:
                # toggle transparency
                self.psys.enableBlend = not self.psys.enableBlend
        
    def onSize(self, win, width, height):
        #print 'onsize: ', win, width, height
        self.width = width
        self.height = height
        self.aspect = width/float(height)
        glViewport(0, 0, self.width, self.height)

    def step(self):
        # inc time
        self.t += 10
        self.psys.step()
        # rotate eye
        if self.rotate:
            self.camera.rotate()
        # restart every 5 seconds 
        if not int(self.t) % 5000:
            self.psys.restart(self.numP)

    def run(self):
        # initializer timer
        glfw.set_time(0)
        t = 0.0
        while not glfw.window_should_close(self.win) and not self.exitNow:
            # update every x seconds
            currT = glfw.get_time()
            if currT - t > 0.01:
                # update time
                t = currT

                # clear
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

                # render
                pMatrix = glutils.perspective(100.0, self.aspect, 0.1, 100.0)
                # modelview matrix
                mvMatrix = glutils.lookAt(self.camera.eye, self.camera.center, 
                                          self.camera.up)
                
                # draw non-transparent object first
                self.box.render(pMatrix, mvMatrix)

                # render
                self.psys.render(pMatrix, mvMatrix, self.camera)

                # step 
                self.step()

                glfw.swap_buffers(self.win)
                # Poll for and process events
                glfw.poll_events()
        # end
        glfw.terminate()

# main() function
def main():
  # use sys.argv if needed
  print('starting particle system...')
  prog = PSMaker()
  prog.run()

# call main
if __name__ == '__main__':
  main()