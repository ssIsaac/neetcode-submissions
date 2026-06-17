class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        posSpeed = []
        for n in range(len(position)):
            posSpeed.append([position[n], speed[n]])
        posSpeed = sorted(posSpeed, reverse=True)
        print(posSpeed)
        

        for position,speed in posSpeed:
            time = (target-position)/speed
            if not fleet or time > fleet[-1]:
                fleet.append(time)
            continue
        
        return len(fleet)




