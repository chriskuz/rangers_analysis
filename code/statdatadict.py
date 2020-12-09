class MoneyPuck:
    import json
    with open("moneypuck_datadict.json", "r") as fp:
        moneypuck_datadict = json.load(fp)

    @staticmethod
    def find(term):
        try:
            return print(MoneyPuck.moneypuck_datadict[term])
        except:
            return print("No such term found in Moneypuck Data Dictionary.")
        # if MoneyPuck.moneypuck_datadict[term]:
        #     return print(MoneyPuck.moneypuck_datadict[term])
        # else:
        #     return print("No such term found in Moneypuck Data Dictionary.")

    @staticmethod
    def terms():
        print("Please reach out through MoneyPuck.com if you have any feedback. No guarantees are made to the quality of the data. NHL data is known to have issues and biases. You are welcome to use this data in any work. Just please cite MoneyPuck.com")

