import paho.mqtt.client

class IOT_Controller:
	configuration = []
	client = None
	mqtt_data =  {}
	def configure(filename, client):
		with open(filename, "r") as file:
			configuration = json.load(file)
		client.connect("localhost", 1883)
		for rule in configuration:
			for condition in rule["conditions"]:
				client.subscribe(condition["topic"])
				print(condition["topic"])
	def run():
		IOT_Controller.client.loop_forever()
		print("run method")
	def on_message(client, userdata, message):
		print("message recieved")
		value = int(message.payload.decode("utf-8"))
		topic = message.topic
		IOT_Controller.mqtt_data[topic] = value
		IOT_Controller.run_rules()
	def run_rules()
		for rule in configuration:
			conditions_met = all(IOT_Controller.evaulate_condition(IOT_Controller.mqtt_data, condition) for condition in rule["conditions"])
			if conditions_met:
				print("do it")
	def evaluate_condition(data, condition)
		topic = condition["topic"]
		value = data.get(topic, None)
		if value == None:
			return False
		comparison = condition["comparison"]
		if condition == "<":
			return value < condition["value"]
		elif condition == ">":
			return value > condition["value"]
		elif condition == ">=":
			return value <= condition["value"]
		elif condition == "<=":
			return value <= condition["value"]
		elif condition == "!=":
			return value != condition["value"]
		elif condition == "==":
			return value == condition["value"]
		
def main():
	IOT_Controller.configure("config.json")
	IOT_Controller.run()
if __name__ == "__main__":
	main()
