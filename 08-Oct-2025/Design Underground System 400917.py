# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    # here is the thing i have id , stationName and time 

    def __init__(self):
        self.hold = defaultdict(list)      
        self.average = defaultdict(list)  

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.hold[id] = [( stationName , t ) ]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        
        name, startTime = self.hold[id][0] 
        del self.hold[id] 
        self.average[(name , stationName)].append(t - startTime)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        item = self.average[(startStation , endStation)]        
        return sum(item) / len(item)
       


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)