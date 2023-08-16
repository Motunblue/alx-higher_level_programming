#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is palindrome
 * @head: head list
 * Return: 1 if palindrome and 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;
	listint_t *next = NULL, *prev = NULL, *tmp = *head;

	if (!head)
		return (0);
	if (!*head)
		return (1);
	while (fast->next && fast->next->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}
	if (fast->next)
		slow = slow->next;
	while (slow)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	while (prev && tmp)
	{
		if (prev->n != tmp->n)
			return (0);
		prev = prev->next;
		tmp = tmp->next;
	}
	return (1);
}
