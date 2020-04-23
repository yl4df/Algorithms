# CS4102 Spring 2020 -- Homework 5
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: yl4df
# Collaborators: 
# Sources: Introduction to Algorithms, Cormen
#################################
class RollerCoaster:
    def __init__(self):
        self.dp=[]
        self.path=[]
        self.start_row=0
        self.start_col=0
        return

    # Use this helper method to fill in nrow * ncol dynamic programming matrix
    # @param1: terrain matrix
    # @param2: row index
    # @param3: column index
    # @param4: the dp matrix which stores results
    # @param5: the bar used to make sure roller coaster going lower
    def dpHelper(self, terrain, i, j, dp, bar):
        # Consider all corner situations as well as always going lower
        if(i<0 or j<0 or i>len(terrain)-1 or j>len(terrain[0])-1 or terrain[i][j]>=bar):
            return 0
        # If the result is stored before, we just take it.
        if(not dp[i][j]==0):
            return dp[i][j]
        # Get the length for adjacent cells
        left = self.dpHelper(terrain, i, j-1, dp, terrain[i][j])
        right = self.dpHelper(terrain, i, j+1, dp, terrain[i][j])
        up = self.dpHelper(terrain, i-1, j, dp, terrain[i][j])
        down = self.dpHelper(terrain, i+1, j, dp, terrain[i][j])
        # Perform comparision. Store max+1 to the current cell.
        list_comparsion = []
        list_comparsion.append(left)
        list_comparsion.append(right)
        list_comparsion.append(up)
        list_comparsion.append(down)
        dp[i][j]=max(list_comparsion)+1

        return dp[i][j]
    # This method is the one you should implement.  It will be called to find the
    # the roller coaster's path.  You may create any additional data structures as fields
    # in this class or write any additional methods you need.
    # 
    # @return the length of the longest drop of the coaster
    def run(self, terrain):
        length=0
        nrow=len(terrain)
        # zero length and none start point for empty matrix
        if(nrow==0):
            self.start_row=None
            self.start_col=None
            return 0
        ncol=len(terrain[0])
        # Initialize dp matrix.
        self.dp=[[0 for j in range(ncol)] for i in range(nrow)]
        # Calculate dp matrix for each cell
        for i in range(0, nrow):
            for j in range(0,ncol):
                if(self.dp[i][j]==0):
                    self.dpHelper(terrain, i, j, self.dp, float('inf'))
                    # Update length if we get a new one
                    length=max(length, self.dp[i][j])
        # Now we start to back track.
        # First we back track to get start point.
        start_row=0
        start_col=0
        for i in range(0, nrow):
            for j in range(0, ncol):
                if(length==self.dp[i][j]):
                    self.path.append(terrain[i][j])
                    start_row=i
                    start_col=j
                    self.start_row = start_row
                    self.start_col = start_col
                    break
            if(len(self.path)==length):
                break
        # Based on the start point, we back track to get the path by subtracting length by one each time.
        back_track_counter = length
        while(back_track_counter>0):
            back_track_counter = back_track_counter - 1
            if(start_row>0):
                if(self.dp[start_row-1][start_col]==back_track_counter):
                    self.path.append(terrain[start_row-1][start_col])
                    start_row = start_row - 1
            if(start_row<len(self.dp)-1):
                if(self.dp[start_row+1][start_col]==back_track_counter):
                    self.path.append(terrain[start_row+1][start_col])
                    start_row = start_row + 1
            if(start_col>0):
                if(self.dp[start_row][start_col-1]==back_track_counter):
                    self.path.append(terrain[start_row][start_col-1])
                    start_col = start_col - 1
            if(start_col<len(self.dp[0])-1):
                if(self.dp[start_row][start_col+1]==back_track_counter):
                    self.path.append(terrain[start_row][start_col+1])
                    start_col = start_col + 1
        return length
    # Get the terrain values in the coaster's main drop path, in order from highest to lowest elevation
    #
    # @return the ordered list of terrain values in the coaster's main drop
    def getCoasterPath(self):
        return self.path

    # Get the row,column starting point for the coaster's main drop path 
    #
    # @return an int[] with the first element being the row and the second being the column
    def getCoasterStart(self):
        return [self.start_row, self.start_col]
