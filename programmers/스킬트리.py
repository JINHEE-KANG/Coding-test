def solution(skill, skill_trees):
    print(f'skill:{skill},skill_trees:{skill_trees}')
    for i in range(len(skill_trees)): #skill_trees i번째 탐색
        ith_skill = skill_trees[-1]
        print(f'{i}th_skill:{ith_skill}')
        for s in range(len(skill)):
            ind = ith_skill.find(skill[s])
            print(f'ind:{ind}')
            if ind != -1:
                ith_skill = ith_skill[ind:]
                print(f'{i}th_skill:{ith_skill[ind:]}')
            else: 
                skill_trees.pop()
                print(f'skill_trees:{skill_trees}')
                break
    
    return len(skill_trees)
