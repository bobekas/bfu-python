from smallPlane import SmallPlane
from mediumPlane import MediumPlane

def main():

	boeing717 = SmallPlane("Boeing 7170", 60, 702, 100, 'Boeing')
	airbusa330 = MediumPlane("AIRBUS A330", 120, 782, 150, 'AIRBUS')
	boeing717.printSpecs()
	boeing717.printMaxSpeed()
	airbusa330.printSpecs()
	airbusa330.printMaxSpeed()

main()
