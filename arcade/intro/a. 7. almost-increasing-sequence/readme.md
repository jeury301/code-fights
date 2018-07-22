## almostIncreasingSequence

### Description
> Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

### Example

* For ```sequence = [1, 3, 2, 1]```, the output should be
```almostIncreasingSequence(sequence) = false```.

	There is no one element in this array that can be removed in order to get a strictly increasing sequence.

* For ```sequence = [1, 3, 2]```, the output should be
```almostIncreasingSequence(sequence) = true```.

	You can remove 3 from the array to get the strictly increasing sequence ```[1, 2]```. Alternately, you can remove ```2``` to get the strictly increasing sequence ```[1, 3]```.

### Input/Output

* #### [execution time limit] 4 seconds (py)

* #### [input] array.integer sequence

 	<i>Guaranteed constraints:</i>

    ```2 ≤ sequence.length ≤ 10^5```,

	```-10^5 ≤ sequence[i] ≤ 10^5```.

* #### [output]
	Return ```true``` if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return ```false```.
