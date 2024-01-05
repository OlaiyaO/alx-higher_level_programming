#include "lists.h"

/** 
 * reverse_list - Reverses a linked list. 
 * @head: Pointer to the head of the linked list. 
 */ 
void reverse_list(listint_t **head) 
{ 
        listint_t *prev = NULL, *current = *head, *next = NULL; 
 
        while (current != NULL) 
        { 
                next = current->next; 
                current->next = prev; 
                prev = current; 
                current = next; 
        } 
 
        *head = prev; 
} 
 
/** 
 * compare_lists - Compares two linked lists. 
 * @head1: Pointer to the head of the first linked list. 
 * @head2: Pointer to the head of the second linked list. 
 * 
 * Return: 1 if the lists are equal, 0 otherwise. 
 */ 
int compare_lists(listint_t *head1, listint_t *head2) 
{ 
        while (head1 != NULL && head2 != NULL) 
        { 
                if (head1->n != head2->n) 
                        return (0); 
 
                head1 = head1->next; 
                head2 = head2->next; 
        } 
 
        return (1); 
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *prev_slow = NULL, *mid = NULL;
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}

	prev_slow->next = NULL;
	reverse_list(&slow);
	result = compare_lists(*head, slow);
	reverse_list(&slow);

	if (mid != NULL)
	{
		prev_slow->next = mid;
		mid->next = slow;
	}
	else
	{
		prev_slow->next = slow;
	}

	return (result);
}
