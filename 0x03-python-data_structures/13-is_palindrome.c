#include <stddef.h>
#include "lists.h"

/* Forward declarations */
void reverse_list(listint_t **head);
int compare_lists(listint_t *head1, listint_t *head2);

/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: double pointer to the head of the linked list
* 
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half = NULL, *mid_node = NULL;
int result = 1;

if (*head != NULL && (*head)->next != NULL)
{
while (fast != NULL && fast->next != NULL)
{
fast = fast->next->next;
prev_slow = slow;
slow = slow->next;
}

if (fast != NULL)
{
mid_node = slow;
slow = slow->next;
}

second_half = slow;
prev_slow->next = NULL;
reverse_list(&second_half);
result = compare_lists(*head, second_half);

reverse_list(&second_half);

if (mid_node != NULL)
{
prev_slow->next = mid_node;
mid_node->next = second_half;
}
else
prev_slow->next = second_half;
}

return (result);
}

/**
* reverse_list - reverses a linked list
* @head: double pointer to the head of the linked list
*/
void reverse_list(listint_t **head)
{
listint_t *prev = NULL, *current = *head, *next;

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
* compare_lists - compares two linked lists
* @head1: pointer to the first linked list
* @head2: pointer to the second linked list
* 
* Return: 1 if they are identical, 0 otherwise
*/
int compare_lists(listint_t *head1, listint_t *head2)
{
while (head1 && head2)
{
if (head1->n == head2->n)
{
head1 = head1->next;
head2 = head2->next;
}
else
return (0);
}

return (head1 == NULL && head2 == NULL);
}
