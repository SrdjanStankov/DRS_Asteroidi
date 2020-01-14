from GameLoop import GameLoop as gl
import Managers as mgr
            
# method for canceling game loop thread
def cancel():
    mgr.Managers.getInstance().input.stopListening()
    gl.getInstance().cancel()

if __name__ == "__main__":
    
    import multiprocessing
    multiprocessing.freeze_support()

    # connect app exit signal to thread stop of game loop
    a = mgr.Managers.getInstance()
    a.app.aboutToQuit.connect(cancel)
    a.scene.show()

    mgr.Managers.getInstance().app.exec_()