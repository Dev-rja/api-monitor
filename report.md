# API Reliability Monitor — SLA Report

> Last updated: **2026-04-08 14:23 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **4/12** &nbsp;|&nbsp; Avg uptime: **80.9%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 100.0% | 306.6 | 588.9 | 1000ms | 0/153 |
| ❌ | `public_apis_list` | 0.0% | 100.0% | 112.1 | 234.1 | 1500ms | 0/153 |
| ❌ | `nasa_apod` | 86.93% | 71.24% | 1654.1 | 10538.0 | 2000ms | 44/153 |
| ❌ | `ipapi_check` | 92.81% | 100.0% | 155.1 | 252.2 | 2500ms | 0/153 |
| ❌ | `open_meteo_weather` | 94.77% | 95.42% | 981.5 | 14877.1 | 2000ms | 7/153 |
| ❌ | `dog_ceo_random` | 98.69% | 73.86% | 1658.3 | 5586.8 | 2500ms | 40/153 |
| ⚠️ | `useless_fact` | 98.69% | 99.35% | 616.8 | 10229.6 | 2500ms | 1/153 |
| ⚠️ | `catfact_random` | 98.69% | 99.35% | 298.4 | 10070.5 | 3000ms | 1/153 |
| ✅ | `agify_name` | 100.0% | 99.35% | 406.0 | 3237.1 | 2000ms | 1/153 |
| ✅ | `rest_countries` | 100.0% | 98.69% | 297.0 | 7269.1 | 2500ms | 2/153 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.35% | 250.5 | 2314.9 | 2000ms | 1/153 |
| ✅ | `coingecko_bitcoin` | 100.0% | 100.0% | 101.0 | 252.0 | 1500ms | 0/153 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `catfact_random` | 00:00 | 5139.3 | 50.0% |
| `dog_ceo_random` | 13:00 | 4153.6 | 100.0% |
| `useless_fact` | 03:00 | 3792.8 | 33.33% |
| `open_meteo_weather` | 05:00 | 3474.6 | 20.0% |
| `nasa_apod` | 13:00 | 3279.6 | 50.0% |
| `nasa_apod` | 11:00 | 2978.7 | 45.45% |
| `nasa_apod` | 20:00 | 2829.3 | 40.0% |
| `nasa_apod` | 22:00 | 2715.0 | 30.0% |
| `open_meteo_weather` | 06:00 | 2675.4 | 16.67% |
| `dog_ceo_random` | 17:00 | 2591.7 | 62.5% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
