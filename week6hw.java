
import java.awt.*;
import hsa.*;

//Boxes

public class CCC2007S2Boxes
{
    static Console c;

    public static void main (String[] args)
    {
	c = new Console ();
	TextInputFile f = new TextInputFile ("s2.1.in");
	int l, w, h, n, j, m;
	Box[] b;
	Box hold;

	n = f.readInt ();
	b = new Box [n];
	for (int i = 0 ; i < n ; i++)
	{
	    l = f.readInt ();
	    w = f.readInt ();
	    h = f.readInt ();
	    b [i] = new Box (l, w, h);
	}

	for (int i = 1 ; i < n ; i++)
	{
	    j = i - 1;
	    hold = b [i];
	    while (j >= 0 && b [j].volume > hold.volume)
	    {
		b [j + 1] = b [j];
		j--;
	    }
	    b [j + 1] = hold;
	}

	m = f.readInt ();
	for (int i = 0 ; i < m ; i++)
	{
	    l = f.readInt ();
	    w = f.readInt ();
	    h = f.readInt ();
	    hold = new Box (l, w, h);
	    j = 0;
	    while (j < n && (hold.l > b [j].l ||
			hold.w > b [j].w ||
			hold.h > b [j].h))
		j++;
	    if (j < n)
		c.println (b [j].volume);
	    else
		c.println ("Item does not fit.");
	}
    }
}

class Box
{
    public int l, w, h;
    public long volume;

    public Box (int a, int b, int c)
    {
	int t;
	l = a;
	w = b;
	h = c;
	if (l > w)
	{
	    t = l;
	    l = w;
	    w = t;
	}
	if (w > h)
	{
	    t = w;
	    w = h;
	    h = t;
	}
	if (l > w)
	{
	    t = l;
	    l = w;
	    w = t;
	}
	volume = l * w * h;
    }
}

// Snow Call


import java.awt.*;
import hsa.*;

public class CCC2005s1SnowCalls
{
    static Console c;

    public static void main (String[] args)
    {
	c = new Console ();
	TextInputFile f = new TextInputFile ("s1.in");
	int n;
	String s;

	n = f.readInt ();
	for (int i = 1 ; i <= n ; i++)
	    c.println (convert (f.readLine ()));
    }

    public static String convert (String s)
    {
	String out;
	int i;
	i = 0;
	out = "";
	while (out.length () < 12)
	{
	    if (s.charAt (i) == '1')
		out = out + "1";
	    else if (s.charAt (i) == '2' || s.charAt (i) == 'A' || s.charAt (i) == 'B' || s.charAt (i) == 'C')
		out = out + "2";
	    else if (s.charAt (i) == '3' || s.charAt (i) == 'D' || s.charAt (i) == 'E' || s.charAt (i) == 'F')
		out = out + "3";
	    else if (s.charAt (i) == '4' || s.charAt (i) == 'G' || s.charAt (i) == 'H' || s.charAt (i) == 'I')
		out = out + "4";
	    else if (s.charAt (i) == '5' || s.charAt (i) == 'J' || s.charAt (i) == 'K' || s.charAt (i) == 'L')
		out = out + "5";
	    else if (s.charAt (i) == '6' || s.charAt (i) == 'M' || s.charAt (i) == 'N' || s.charAt (i) == 'O')
		out = out + "6";
	    else if (s.charAt (i) == '7' || s.charAt (i) == 'P' || s.charAt (i) == 'Q' || s.charAt (i) == 'R' || s.charAt (i) == 'S')
		out = out + "7";
	    else if (s.charAt (i) == '8' || s.charAt (i) == 'T' || s.charAt (i) == 'U' || s.charAt (i) == 'V')
		out = out + "8";
	    else if (s.charAt (i) == '9' || s.charAt (i) == 'W' || s.charAt (i) == 'X' || s.charAt (i) == 'Y' || s.charAt (i) == 'Z')
		out = out + "9";
	    else if (s.charAt (i) == '0')
		out = out + "0";
	    i++;
	    if (out.length () == 3 || out.length () == 7)
		out = out + "-";
	}
	return out;
    }
}
