#include "lists.h"

/**
 * reverse_list - reverses the second half of the list
 * @middle: pointer to the middle of the list
 */
void reverse_list(listint_t **middle)
{
	listint_t *prev = NULL, *next = NULL, *current = *middle;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*middle = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list to be checked
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle = *head, *speedy = *head;

	if (!middle || !middle->next)
		return (1);

	while (middle && speedy && speedy->next)
	{
		middle = middle->next;
		speedy = speedy->next->next;
	}
	reverse_list(&middle);
	speedy = *head;
	while (middle)
	{
		if (speedy->n != middle->n)
			return (0);
		speedy = speedy->next;
		middle = middle->next;
	}
	reverse_list(&middle);
	return (1);
}
