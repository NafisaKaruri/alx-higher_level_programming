#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: the pointer to the head of the linked list
 * @number: the number to be inserted to the new node
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;
	else if ((*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next && (current->next->n < number))
			current = current->next;
		temp = current->next;
		current->next = new_node;
		new_node->next = temp;
	}
	return (new_node);
}
