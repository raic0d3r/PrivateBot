<div class="entrytext" style="height: auto !important;">
            	<h1 class="page-title">How to install Tor and create Tor hidden service on Windows</h1>        		<div class="content-ver-sep"> </div>
				

<div class="0b20205ac99e89c6cabdb919fd9d1a8a" data-index="1" style="float:none;margin:10px 0 10px 0;text-align:center">
</div>
<h2 style="text-align:justify">
	Where to download Tor for Windows<br>
</h2>
<p style="text-align:justify">
	If you need a browser with Tor, that is, if you are sufficient that you can have another IP when surfing the Internet or want to bypass regional restriction, then you need <strong>Tor Browser</strong>, download it from the <a href="https://www.torproject.org/download/download" target="_blank">official site</a>. There already is everything you need for anonymous surfing in the web and everything is already set up.
</p>
<p style="text-align:justify">
	If you want to install Tor as a service on Windows, then you need <strong>Expert Bundle</strong>. It can be downloaded from the <a href="https://www.torproject.org/download/download" target="_blank">same page</a> of the official website. Next we will talk only about the Expert Bundle.
</p>
<p style="text-align:justify">
	From the downloaded archive (in my case, the file is called tor-win32-0.3.3.7.zip), unpack the <strong>Tor </strong>folder to the root of drive <strong>C</strong>.
</p>
<h2 style="text-align:justify">
	How to launch Tor on Windows<br>
</h2>
<p style="text-align:justify">
	Tor can be started once, or set as NT service, which will be launched each time your computer booting. Consider a one-time launch. Open the Windows command prompt, to do this, press&nbsp;<strong>Win+x</strong> and select "<strong>Windows PowerShell (Administrator)</strong>" there.
</p>
<p style="text-align:justify">
	In the window that opens, type
</p>
<div><div id="highlighter_148691" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	Wait until Tor completes his business:
</p>
<p style="text-align:justify">
	<a href="https://miloserdov.org/wp-content/uploads/2018/07/41.jpg"><img loading="lazy" alt="" class="alignnone size-full wp-image-1843" height="343" src="https://miloserdov.org/wp-content/uploads/2018/07/41.jpg" width="1183" srcset="https://miloserdov.org/wp-content/uploads/2018/07/41.jpg 1183w, https://miloserdov.org/wp-content/uploads/2018/07/41-1000x290.jpg 1000w, https://miloserdov.org/wp-content/uploads/2018/07/41-768x223.jpg 768w" sizes="(max-width: 1183px) 100vw, 1183px" data-pagespeed-lsc-url="https://miloserdov.org/wp-content/uploads/2018/07/41.jpg"></a>
</p>
<p style="text-align:justify">
	Tor already works! But it will end if you close the window. For Tor to work constantly, it needs to be installed as a service.
</p>
<h2 style="text-align:justify">
	Installing Tor as a Windows Service<br>
</h2>
<p style="text-align:justify">
	To install the service, simply run the command:
</p>
<div><div id="highlighter_438485" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe --service </code><code class="bash functions">install</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	You can adjust&nbsp;the service using various <a href="https://www.torproject.org/docs/tor-manual-dev.html.en" target="_blank">Tor command-line options</a>.
</p>

<div class="0b20205ac99e89c6cabdb919fd9d1a8a" data-index="3" style="float:none;margin:10px 0 10px 0;text-align:center">

</div>

<p style="text-align:justify">
	We need a configuration file, so create it in the <strong>C:\Tor\,</strong> directory, this file should be named <strong>torrc</strong>:
</p>
<div><div id="highlighter_893976" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash functions">echo</code><code class="bash plain">( &gt; C:\Tor\torrc</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	To check if the service with the settings file starts (it does not contain errors), you can use this command:
</p>
<div><div id="highlighter_594810" class="syntaxhighlighter  bash "><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe -f </code><code class="bash string">"C:\Tor\torrc"</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	Now install the Tor service, which will read the settings from the <strong>C:\Tor\torrc</strong> file:
</p>
<div><div id="highlighter_303739" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe --service </code><code class="bash functions">install</code> <code class="bash plain">-options -f </code><code class="bash string">"C:\Tor\torrc"</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	Remember that you must specify options after the <strong>-options</strong> flag, otherwise they will be ignored.
</p>
<p style="text-align:justify">
	To start and stop the service, use the following commands:
</p>
<div><div id="highlighter_932314" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe --service start</code></div><div class="line number2 index1 alt1"><code class="bash plain">C:\Tor\tor.exe --service stop</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	To remove the service:
</p>
<div><div id="highlighter_172193" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">C:\Tor\tor.exe --service stop</code></div><div class="line number2 index1 alt1"><code class="bash plain">C:\Tor\tor.exe --service remove</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	Note that you must first stop the service and then delete it.
</p>
<p style="text-align:justify">
	By default, the Tor service listens on port <strong>9050</strong>, so you can check whether it is started by a command that shows if port 9050 is listened:
</p>
<div><div id="highlighter_496877" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash functions">netstat</code> <code class="bash plain">-aon | findstr </code><code class="bash string">":9050"</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	You can also use the following command:
</p>
<div><div id="highlighter_180409" class="syntaxhighlighter  bash"><table border="0" cellpadding="0" cellspacing="0"><tbody><tr><td class="gutter"><div class="line number1 index0 alt2">1</div><div class="line number2 index1 alt1">2</div></td><td class="code"><div class="container"><div class="line number1 index0 alt2"><code class="bash plain">cmd</code></div><div class="line number2 index1 alt1"><code class="bash keyword">for</code> <code class="bash plain">/f</code> <code class="bash string">"tokens=1,2,3,4,5*"</code> <code class="bash plain">%i </code><code class="bash keyword">in</code> <code class="bash plain">(</code><code class="bash string">'netstat -aon ^| findstr ":9050" ^| findstr /i listening'</code><code class="bash plain">) </code><code class="bash keyword">do</code> <code class="bash functions">echo</code> <code class="bash plain">%j %l &amp; @tasklist | findstr %m</code></div></div></td></tr></tbody></table></div></div>
<p style="text-align:justify">
	<a href="https://miloserdov.org/wp-content/uploads/2018/07/49.jpg"><img loading="lazy" alt="" class="alignnone size-full wp-image-1856" height="279" src="https://miloserdov.org/wp-content/uploads/2018/07/49.jpg" width="1226" srcset="https://miloserdov.org/wp-content/uploads/2018/07/49.jpg 1226w, https://miloserdov.org/wp-content/uploads/2018/07/49-1000x228.jpg 1000w, https://miloserdov.org/wp-content/uploads/2018/07/49-768x175.jpg 768w" sizes="(max-width: 1226px) 100vw, 1226px" data-pagespeed-lsc-url="https://miloserdov.org/wp-content/uploads/2018/07/49.jpg"></a>
</p>
<p style="text-align:justify">
	Now, when the Tor service is installed and running, several recipes will be shown, how it can be used.
</p>
