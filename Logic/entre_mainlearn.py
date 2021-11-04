import learn_mainpy


def back_to_main(self):
    self.exit_window = learn_mainpy.MainLearn(self.module_id)
    self.hide()
    self.exit_window.show()
