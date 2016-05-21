# Source: https://codefights.com/challenge/CmopfLedECCKbCGMG

<div classfiletype on="task-description" flex="">
	<marked-element>
		<p>You're given an <code>equation</code> that consists of numbers, parenthesis and operations <code>'+'</code> and <code>'-'</code>. But you don't want just to calculate it's result the way ordinary people do. You have your own rules of calculation!</p>
		<p>Firstly, you remove all whitespaces from the equation (who needs them anyway)? Secondly, you calculate the sum of even digits in it. If there's a <code>'-'</code> symbol just before the digit, you consider it as a negative number. Thirdly, you calculate the sum of odd numbers, paying attention to the <code>'-'</code> symbols as well. Finally, you subtract the sum of the odd numbers from the sum of even numbers. The obtained result is the result of the equation.</p>
		<p>Now you need to write a program that does this kind of calculation for you. Given an <code>equation</code>, calculate it's value with your very own algorithm.</p>
		<p>
		<strong>Example</strong>
		</p>
		<ul>
			<li>
				<p>For <code>equation = "(-100) + 100 - (-200) + 1"</code>, the output should be<br>
				<code>SumtheDifference(equation) = -3</code>.</p>
				<ul>
					<li>there's only one even digit, which is <code>-2</code>;</li>
					<li>odd digits sum up to <code>-1 + 1 + 1 = 1</code>;</li>
					<li>their difference is <code>-2 - 1 = -3</code>.</li>
				</ul>
			</li>
			<li>
				<p>For <code>equation = "(-25) + (-75) + 50 - 40 - (22 + 2)"</code>, the output should be<br>
				<code>SumtheDifference(equation) = -8</code>.</p>
				<ul>
					<li>even digits sum up to <code>-2 - 4 + 2 + 2 + 2 = 0</code>;</li>
					<li>odd digits sum up to <code>5 - 7 + 5 + 5 = 8</code>;</li>
					<li>their difference is <code>0 - 8 = -8</code>.</li>
				</ul>
			</li>
		</ul>
		<ul>
			<li>
				<p>
				<strong>[input] string equation</strong>
				</p>
				<p>An equation (not necessarily correct) consisting of digits, parenthesis and operators <code>'-'</code> and <code>'+'</code>.<br>
				<code>0 ≤ equation.length ≤ 100</code>.</p>
			</li>
			<li>
				<p>
				<strong>[output] integer</strong>
				</p>
				<p>Result of the equation.</p>
			</li>
		</ul>
	</marked-element>
</div>