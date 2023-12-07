from typing import List
from ..models.models import Expense, ExpenseSplit, Transaction
from heapq import heapify, heappop, heappush

class MaxHeap:

    @staticmethod
    def heappush(heap, element):
        new_ele = list(element)
        new_ele[0] = new_ele[0] * - 1
        heappush(heap, tuple(new_ele))
    
    @staticmethod
    def heappop(heap):
        new_ele = list(heappush(heap))
        new_ele[0] = new_ele[0] * - 1
        return tuple(new_ele)

class SettleUpService():

    def settle_up(self, expenses:List[Expense]) -> List[Transaction]:

        transactions : List[Transaction] = []
        is_group = expenses[0].is_group_expense
        group = expenses[0].group

        user_total = self._get_total(expenses)
        
        paid_user = []
        wiil_pay_user = []

        for user in user_total.keys():
            if user_total[user] > 0:
                element = (user_total[user] * - 1, user_total[user], user)
                heappush(paid_user, element)
            elif user_total[user] < 0:
                element = (user_total[user], user_total[user], user)
                heappush(wiil_pay_user, element)
        
        while len(paid_user) > 0:
            paid_element = heappop(paid_user)
            will_pay_element =  heappop(wiil_pay_user)

            if abs(paid_element[0]) > abs(will_pay_element[0]):
                rem_amount = abs(paid_element[0]) - abs(will_pay_element[0])
                element = ( rem_amount* - 1, rem_amount,paid_element[2])
                heappush(paid_user, element)

                transaction = Transaction(is_group_transaction=is_group, group=group, received_by=paid_element[2], paid_by=will_pay_element[2],amount=rem_amount,is_settled=False)
                transactions.append(transaction)

            elif abs(will_pay_element[0]) > abs(paid_element[0]):
                rem_amount = abs(will_pay_element[0]) - abs(paid_element[0])
                element = ( rem_amount, rem_amount,paid_element[2])
                heappush(wiil_pay_user, element)
                transaction = Transaction(is_group_transaction=is_group, group=group, received_by=paid_element[2], paid_by=will_pay_element[2],amount=rem_amount,is_settled=False)
                transactions.append(transaction)

        return transactions


        
    

    def _get_total(self, expenses:List[Expense]):

        user_total = {}

        for expense in expenses:

            if expense.paid_by not in user_total:
                user_total[expense.paid_by] = 0.0
            
            user_total[expense.paid_by] += expense.paid_amount

            for each_split in expense.exppense_splits:
                if each_split.user not in user_total:
                    user_total[each_split.user] = 0.0

                user_total[each_split.user] -= each_split.split_amount
        
        return user_total
