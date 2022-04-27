
def configure_app_output(prefix):

  def belle(msg):
    print(prefix + " > " + msg)

  return belle

app_output1 = configure_app_output("DemoApp")
app_output2 = configure_app_output("AnotherApp")

app_output1("one")
app_output1("two")

app_output2("one")
app_output2("two")

app_output1("three")


app_output2("three")
