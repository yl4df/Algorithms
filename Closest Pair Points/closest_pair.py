# CS4102 Spring 2020 - Homework 3
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the
# comments at the top of each submitted file. Do not share written notes,
# documents (including Google docs, Overleaf docs, discussion notes, PDFs), or
# code. Do not seek published or online solutions, including pseudocode, for
# this assignment. If you use any published or online resources (which may not
# include solutions) when completing this assignment, be sure to cite them. Do
# not submit a solution that you are unable to explain orally to a member of
# the course staff. Any solutions that share similar text/code will be
# considered in breach of this policy. Please refer to the syllabus for a
# complete description of the collaboration policy.
#################################
# Your Computing ID: yl4df
# Collaborators: n/a
# Sources: Introduction to Algorithms, Cormen
#################################
import math
import sys

class ClosestPair:
    def __init__(self):
        return

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distance
    # and return that value from this method
    #
    # @return the distance between the closest pair 
    def compute(self, file_data):
        point_list = []
        for line in file_data:
            tuple=line.split()
            point_list.append((float(tuple[0]),float(tuple[1])))
        # Sort by x coordinate. Run Time Theta(n*logn)
        point_list.sort()
        return self.divide_conquer(point_list)

    # Helper Function to calculate distance. Run time Theta(1)
    def distance(self,X, Y):
        return float(math.sqrt((X[0] - Y[0])**2 + (X[1] - Y[1])**2))

    # Helper Function to merge two sorted list. Run time Theta (n) because it transverses all points once.
    def merge(self, l1, l2):
        total_points = []
        while l1 and l2:
            if(l1[0][1] < l2[0][1]):
                total_points.append(l1.pop(0))
            else:
                total_points.append(l2.pop(0))
        if(len(l1)!=0):
            total_points+=l1
        elif(len(l2)!=0):
            total_points+=l2
        return total_points

    def divide_conquer(self, point_list):
        if(len(point_list)<=1):
            print("Invalid Input!")
            return
        # Base Case 1: two points in list
        if (len(point_list)==2):
            point_list.sort(key=lambda k: k[1])
            return self.distance(point_list[0], point_list[1])
        # Base Case 2: three points in list
        elif (len(point_list)==3):
            point_list.sort(key=lambda k: k[1])
            return min(self.distance(point_list[0], point_list[1]), self.distance(point_list[1], point_list[2]), self.distance(point_list[0], point_list[2]))
        # Divide the list by median x coordinate. Run time Theta(1)
        median_index=(int(len(point_list)/2))
        if(len(point_list)%2==0):
            left_points = point_list[:median_index]
            right_points = point_list[median_index:]
            median_x_coordinate=(point_list[median_index-1][0]+point_list[median_index][0])/2
        elif(len(point_list)%2!=0):
            left_points = point_list[:(median_index+1)]
            right_points = point_list[(median_index+1):]
            median_x_coordinate=point_list[median_index][0]
        # Recursively Find the min distance on left and right
        left_min_dist = self.divide_conquer(left_points)
        right_min_dist = self.divide_conquer(right_points)
        delta=min(left_min_dist, right_min_dist)
        # Merge sorted list. Run time Theta(n) as stated above.
        total_points=self.merge(left_points, right_points)
        # Build Runway. Run time Theta(n) as it transverses all points once.
        runway=[]
        for point in total_points:
            if (point[0]>=median_x_coordinate-delta and point[0]<=median_x_coordinate+delta):
                runway.append(point)
        # Find min distance in runway. Run time Theta(n) as it transverses all points and all 15 points above it.
        runway_min_dist=sys.float_info.max
        for i in range(0,len(runway)):
            for j in range(i+1, min(len(runway), i + 16)):
                runway_min_dist=min(runway_min_dist, self.distance(runway[i], runway[j]))
        return min(left_min_dist, right_min_dist, runway_min_dist)
