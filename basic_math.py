#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """
    maxx=-9999999
    for k in range(0,len(number_list)):
        if number_list[k]>maxx:
            maxx=number_list[k]

    greatest_number = maxx
    return greatest_number


def get_smallest(number_list):
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """
    minn=9999999
    for k in range(0,len(number_list)):
        if number_list[k]<minn:
            minn=number_list[k]

    smallest_number = minn
    return smallest_number


def get_mean(number_list):
    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    summ=0.0
    for k in range(0,len(number_list)):
        summ+=float(number_list[k])
    mean = summ/len(number_list)
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    s=sorted(number_list)
    tmp=len(number_list)
    index=tmp//2
    if tmp%2==1:
        median=s[index]
    else:
        median=(s[index-1]+s[index])/2.0

    return median
