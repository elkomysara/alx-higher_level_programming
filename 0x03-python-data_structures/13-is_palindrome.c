#include "lists.h"
#include <stddef.h>  /* Include for NULL */

/* Function prototypes */
void reverse_list(listint_t **head);
int compare_lists(listint_t *head1, listint_t *head2);

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *second_half = NULL, *mid_node = NULL;
    int result = 1;

    if (*head && (*head)->next)
    {
        while (fast && fast->next)
        {
            fast = fast->next->next;
            prev_slow = slow;
            slow = slow->next;
        }

        if (fast)
        {
            mid_node = slow;
            slow = slow->next;
        }

        second_half = slow;
        prev_slow->next = NULL;
        reverse_list(&second_half);
        result = compare_lists(*head, second_half);

        reverse_list(&second_half);

        if (mid_node)
        {
            prev_slow->next = mid_node;
            mid_node->next = second_half;
        }
        else
            prev_slow->next = second_half;
    }

    return result;
}

void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

int compare_lists(listint_t *head1, listint_t *head2)
{
    while (head1 && head2)
    {
        if (head1->n != head2->n)
            return 0;

        head1 = head1->next;
        head2 = head2->next;
    }

    return (head1 == NULL && head2 == NULL);
}
