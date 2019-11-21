class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        if commands is None or len(commands) == 0:
            return 0

        '''
            -2：向左转 90 度
            -1：向右转 90 度
            1 <= x <= 9：向前移动 x 个单位长度
        '''
        obstacles = set(map(tuple, obstacles))

        current_direction = 'North'
        current_position = [0,0]
        onestep_former_position = current_position
        max_distance = 0

        for command in commands:
            # 改变方向的命令
            if command == -1 or command == -2:
                current_direction = self.changeDirection(current_direction, command)
            # 移动的命令
            else:
                for step in range(command):
                    # 将上一步的坐标记录下来
                    onestep_former_position = list(current_position)

                    max_distance = max(max_distance, onestep_former_position[0]**2 + onestep_former_position[1]**2)

                    if current_direction == 'North':
                        current_position[1] += 1

                    elif current_direction == 'South':
                        current_position[1] -= 1

                    elif current_direction == 'East':
                        current_position[0] += 1

                    else:
                        current_position[0] -= 1

                    '''
                    必须注意使用集合Set作为对障碍物使用的数据结构，以便我们可以有效地检查下一步是否受阻。如果不这样做，我们检查
                    该点是障碍点吗可能会慢大约10000倍。
                    '''
                    if tuple(current_position) in obstacles:
                        current_position = list(onestep_former_position)
                        break

                max_distance = max(max_distance, current_position[0] ** 2 + current_position[1] ** 2)

        return max_distance


    def changeDirection(self, current_direction, command):
        if current_direction == 'North':
            if command == -2:
                return 'West'
            else:
                return 'East'

        elif current_direction == 'West':
            if command == -2:
                return 'South'
            else:
                return 'North'

        elif current_direction == 'South':
            if command == -2:
                return 'East'
            else:
                return 'West'

        elif current_direction == 'East':
            if command == -2:
                return 'North'
            else:
                return 'South'

