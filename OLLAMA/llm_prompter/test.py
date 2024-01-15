import re


text ='''
Title: The Magical World of Pixels and Animation: A Journey Through Gaming and Live Streaming

Context:
In today's fast-paced world, it's not uncommon to find yourself seeking a little escape from reality. Whether you're looking for an adrenaline rush or just wanting to unwind, there are countless ways to entertain yourself. Two popular pastimes that have captured the hearts of millions around the globe are video games and live streaming. In this blog post, we will embark on a magical journey through the world of pixels and animation, exploring the captivating realms of video games and live streaming, with a hint of anime thrown in for good measure.

First, let's dive into the realm of video games. Video games have evolved significantly over the decades, from simple 2D pixel art to the stunningly realistic 3D graphics we see today. They provide a diverse range of experiences, allowing us to explore fantastical worlds, engage in epic battles, and even save the day as our favorite heroes. Many video games also incorporate elements of anime, with their rich storytelling, dynamic characters, and breathtaking visuals drawing inspiration from this beloved art form.

Now, let's delve into the world of live streaming. Live streaming has revolutionized the way we consume content, enabling us to connect with our favorite content creators in real-time. Whether you're watching someone play the latest video game release or learning a new skill from a talented artist, live streaming offers an unparalleled level of engagement and interaction. Many live streamers also incorporate anime into their content, sharing their passion for this art form with their audiences and creating unique, immersive experiences.

So, how do video games and live streaming intertwine? The answer is simple: community. Both video games and live streaming bring people together, allowing us to connect with others who share our interests and passions. Through gaming communities and live streaming platforms, we can form friendships, learn new skills, and even collaborate on projects. In many cases, these connections can lead to lifelong friendships and even careers in the entertainment industry.

In conclusion, the world of pixels and animation offers a rich tapestry of experiences, from the immersive worlds of video games to the engaging real-time interactions of live streaming. By exploring this magical realm, we can discover new passions, connect with like-minded individuals, and find endless entertainment. So why not join us on this journey? Who knows where it might take you!

End Note:
This blog post aims to provide readers with an engaging and informative look into the worlds of video games, live streaming, and anime. It is structured in a way that flows seamlessly from one topic to another, providing context and connections between each subject. The use of vivid language and personal anecdotes helps to bring the content to life, making it relatable and engaging for readers. Additionally, the post includes images and videos related to each topic, adding visual interest and breaking up the text. Overall, this blog post is designed to be a comprehensive and enjoyable exploration of the magical world of pixels and animation.
'''

pattern_title = re.compile(r'[tT]itle\s?:\s?.*')
pattern_context = re.compile(r'[cC]ontext\s?:\s?.*', re.DOTALL)

title = pattern_title.search(text)

context = pattern_context.search(text)

print(title[0])
print("################")
print(context[0])

