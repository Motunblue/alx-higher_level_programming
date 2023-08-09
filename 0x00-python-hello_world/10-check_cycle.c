#include "lists.h"

/**
 * check_cycle - Checks if a single linked list has a cycle
 * @list: The single linked list
 * Return: 0 if no cycle and 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = list;

	while (tmp)
	{
		if (tmp->next == list)
			return (1);
		tmp = tmp->next;
	}
	return (0);
}
