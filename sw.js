<main class="flex-grow container mx-auto px-4 py-10">
<div class="flex flex-col lg:flex-row max-w-6xl mx-auto gap-10">
    <div class="w-full lg:w-1/2 bg-white p-8 rounded-lg shadow-sm">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">Generate Your AI Book</h1>
        <form id="book-form" class="space-y-6">
                  <div>
                      <label for="api_key" class="block mb-2 text-sm font-medium text-gray-700">OpenAI API Key</label>
                      <input type="password" id="api_key" name="api_key" required class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary focus:border-transparent transition">
                  </div>
                  <div>
                      <label for="model" class="block mb-2 text-sm font-medium text-gray-700">Model</label>
                      <select id="model" name="model" required class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary focus:border-transparent transition">
                          <option value="gpt-3.5-turbo" data-price="0">GPT-3.5 Turbo</option>
                          <option value="gpt-4o-mini" data-price="2000">GPT-4o Mini</option>
                          <option value="gpt-4o" data-price="2000">GPT-4o</option>
                          <option value="gpt-4o-mini-2024-07-18" data-price="2000">GPT-4o Mini (2024-07-18)</option>
                      </select>
                  </div>
                  <div>
                      <label for="language" class="block mb-2 text-sm font-medium text-gray-700">Language</label>
                      <select id="language" name="language" required class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary focus:border-transparent transition">
                          <option value="english">English</option>
                          <option value="hindi">Hindi(Experimental)</option>
                          <option value="spanish">Spanish</option>
                      </select>
                  </div>
                  <div>
                      <label for="topic" class="block mb-2 text-sm font-medium text-gray-700">Book Topic</label>
                      <input type="text" id="topic" name="topic" required class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary focus:border-transparent transition">
                  </div>
                  <div>
                      <label for="word_count" class="block mb-2 text-sm font-medium text-gray-700">Target Word Count</label>
                      <input type="number" id="word_count" name="word_count" value="10000" required class="w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-primary focus:border-transparent transition">
                  </div>
                  <button type="submit" class="w-full bg-indigo-950	 text-white py-3 rounded-md hover:bg-blue-600 transition font-medium">Generate Book</button>
              </form>
        <div id="progress" class="mt-4 text-secondary text-center"></div>
        <div id="error-message" class="mt-4 p-4 bg-red-100 text-red-700 rounded-md text-center font-medium hidden"></div>
    </div>
    <div class="w-full lg:w-1/2 bg-white shadow-sm rounded-lg overflow-hidden">
        <div class="h-[600px] p-8 overflow-auto">
            <div class="page-content"></div>
        </div>
    </div>
</div>
</main>