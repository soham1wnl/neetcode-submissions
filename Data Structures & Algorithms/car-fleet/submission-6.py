class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars=[(p,s) for p,s in zip(position,speed)]
        cars.sort(reverse=True)

        stax=[]

        for p,s in cars:
            arv=(target-p)/s

            if not stax or arv>stax[-1]:
                stax.append(arv)

        return len(stax)